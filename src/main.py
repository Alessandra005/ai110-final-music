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
    query_to_preferences,
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
    log("System started")
    log(f"Loaded {len(songs)} songs")

    user_query = input("Enter what kind of music you want: ")
    log(f"User query: {user_query}")

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

        log(f"Recommended: {song['title']} | Score: {score:.2f} | Confidence: {confidence}")

    log(f"Retrieved {len(retrieved_songs)} songs")

    # 3-PROFILE EXPERIMENT 
    profiles = [
        "sad indie low-energy music",
        "high energy gym edm or rock",
        "happy upbeat dance pop"
    ]

    print("\n=== Running 3 Profile Experiments ===\n")

    for profile in profiles:
        print(f"\n--- Profile: {profile} ---")
        log(f"Running profile test: {profile}")

        retrieved = retrieve_songs_by_query(profile, songs)
        prefs = query_to_preferences(profile)

        recs = recommend_songs(prefs, retrieved, k=3, strategy=strategy)

        for song, score, _ in recs:
            print(f"{song['title']} - {score:.2f}")
        print()


if __name__ == "__main__":
    main()
