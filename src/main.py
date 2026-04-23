"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from src.rag import (
    retrieve_songs_by_query,
    generate_explanation,
    compute_confidence,
    query_to_preferences,   # 👈 ADD THIS
)
from src.logger import log
from src.recommender import (
    EnergyFocusedStrategy,
    GenreFirstStrategy,
    MoodFirstStrategy,
    load_songs,
    recommend_songs,
)


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_query = input("Enter what kind of music you want: ")

    # RAG: retrieve relevant songs first
    retrieved_songs = retrieve_songs_by_query(user_query, songs)

    if not retrieved_songs:
        print("No songs found for that query.")
        return

    strategy = EnergyFocusedStrategy()

    user_prefs = query_to_preferences(user_query)

    recommendations = recommend_songs(
        user_prefs,
        retrieved_songs,
        k=5,
        strategy=strategy,
    )

    print("\nTop recommendations:\n")

    for song, score, _ in recommendations:
        explanation = generate_explanation(user_query, song)
        confidence = compute_confidence(score)

        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Confidence: {confidence}")
        print(f"AI Explanation: {explanation}")
        print()

        log(f"Recommended {song['title']} with score {score}")


if __name__ == "__main__":
    main()
