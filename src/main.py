"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from tabulate import tabulate
from src.rag import (
    retrieve_songs_by_query,
    generate_explanation,
    compute_confidence,
    query_to_preferences,
)
from src.logger import log
from src.recommender import (
    load_songs,
    GenreFirstStrategy,
    MoodFirstStrategy,
    EnergyFocusedStrategy,
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

    print("\nChoose ranking mode:")
    print("1 = Energy-Focused")
    print("2 = Genre-First")
    print("3 = Mood-First")

    mode = input("Enter mode (1/2/3): ")

    if mode == "1":
        strategy = EnergyFocusedStrategy()
        mode_name = "Energy-Focused"
    elif mode == "2":
        strategy = GenreFirstStrategy()
        mode_name = "Genre-First"
    elif mode == "3":
        strategy = MoodFirstStrategy()
        mode_name = "Mood-First"
    else:
        print("Invalid input. Defaulting to Energy-Focused.")
        strategy = EnergyFocusedStrategy()
        mode_name = "Energy-Focused"

    log(f"Ranking mode selected: {mode_name}")

    user_prefs = query_to_preferences(user_query)

    recommendations = recommend_songs(
        user_prefs,
        retrieved_songs,
        k=5,
        strategy=strategy,
    )

    table_data = []

    for song, score, _ in recommendations:
        explanation = generate_explanation(user_query, song)
        confidence = compute_confidence(score)

        table_data.append([
            song["title"],
            song["artist"],
            f"{score:.2f}",
            confidence,
            explanation
        ])

        log(f"Recommended: {song['title']} | Score: {score:.2f} | Confidence: {confidence}")

    print("\nTop Recommendations:\n")
    print(tabulate(
        table_data,
        headers=["Title", "Artist", "Score", "Confidence", "Reason"],
        tablefmt="grid"
    ))

    log(f"Retrieved {len(retrieved_songs)} songs")

    # 3-PROFILE EXPERIMENT
    profiles = [
        {
            "name": "Sad Indie Low-Energy Listener",
            "query": "sad indie low-energy music",
            "strategy": MoodFirstStrategy()
        },
        {
            "name": "High Energy Gym Listener",
            "query": "high energy gym electronic workout music",
            "strategy": EnergyFocusedStrategy()
        },
        {
            "name": "Happy Dance Pop Listener",
            "query": "happy upbeat dance pop music",
            "strategy": GenreFirstStrategy()
        }
    ]

    print("\n=== Running 3 Profile Experiments ===\n")

    for profile in profiles:
        print(f"\n--- Profile: {profile['name']} ---")

        retrieved = retrieve_songs_by_query(profile["query"], songs)

        if not retrieved:
            print("No songs found.")
            continue

        prefs = query_to_preferences(profile["query"])

        recs = recommend_songs(
            prefs,
            retrieved,
            k=3,
            strategy=profile["strategy"]
        )

        for song, score, reasons in recs:
            print(f"{song['title']} - {score:.2f}")
            print("Reasons:", ", ".join(reasons[:2]))


if __name__ == "__main__":
    main()
