from typing import List, Dict
from src.logger import log

KEYWORD_MAP = {
    "sad": ["sad", "melancholy", "chill", "emotional"],
    "happy": ["happy", "upbeat", "dance"],
    "chill": ["chill", "lofi", "calm"],
    "rock": ["rock"],
    "pop": ["pop"],
    "intense": ["intense", "energetic"],
}


def retrieve_songs_by_query(query: str, songs: List[Dict]) -> List[Dict]:
    query = query.lower()
    results = []

    expanded_terms = []
    for key, values in KEYWORD_MAP.items():
        if key in query:
            expanded_terms.extend(values)

    if not expanded_terms:
        expanded_terms = [query]

    for song in songs:
        song_text = f"{song['genre']} {song['mood']}".lower()

        if any(term in song_text for term in expanded_terms):
            results.append(song)

    log(f"Query: {query} | Expanded: {expanded_terms} | Results: {len(results)}")

    return results


def generate_explanation(query: str, song: Dict) -> str:
    """
    Simulated AI explanation (you can upgrade later with OpenAI API)
    """
    explanation = f"This song matches your request '{query}' because it is {song['mood']} and in the {song['genre']} genre."
    
    log(f"Generated explanation for song: {song['title']}")
    return explanation


def compute_confidence(score: float) -> float:
    """
    Simple confidence score (0–1 normalized)
    """
    confidence = min(score / 5.0, 1.0)
    return round(confidence, 2)

def query_to_preferences(query: str) -> Dict:
    """
    Converts natural language into structured preferences
    """
    query = query.lower()

    prefs = {
        "favorite_genre": "",
        "favorite_mood": "",
        "target_energy": 0.5,
        "target_valence": 0.5,
        "target_danceability": 0.5,
        "target_acousticness": 0.5,
    }

    # keyword detection
    if any(word in query for word in ["sad", "emotional", "cry"]):
        prefs["favorite_mood"] = "chill"
        prefs["target_valence"] = 0.3

    if any(word in query for word in ["happy", "fun", "upbeat"]):
        prefs["favorite_mood"] = "happy"
        prefs["target_valence"] = 0.8

    if any(word in query for word in ["rock", "metal"]):
        prefs["favorite_genre"] = "rock"
        prefs["target_energy"] = 0.9

    if any(word in query for word in ["chill", "lofi", "study", "relax"]):
        prefs["favorite_genre"] = "lofi"
        prefs["target_energy"] = 0.3
        prefs["target_acousticness"] = 0.7

    return prefs