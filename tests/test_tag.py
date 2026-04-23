from src.rag import retrieve_songs_by_query

def test_retrieval_returns_results():
    songs = [
        {"genre": "pop", "mood": "happy"},
        {"genre": "rock", "mood": "intense"}
    ]

    results = retrieve_songs_by_query("pop", songs)
    assert len(results) > 0