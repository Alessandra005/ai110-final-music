from typing import List, Dict
from src.logger import log

KEYWORD_MAP = {
    "sad": ["sad", "melancholy", "chill", "emotional"],
    "happy": ["happy", "upbeat", "dance"],
    "chill": ["chill", "lofi", "calm"],
    "rock": ["rock"],
    "pop": ["pop"],
    "intense": ["intense", "energetic"],
    "gym": ["energetic", "intense", "edm", "high energy"],
    "edm": ["edm", "electronic", "dance"],
    "study": ["lofi", "chill", "calm"],
    "romantic": ["romantic", "love", "soft"],
    "angry": ["angry", "aggressive", "intense"],
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
        song_text = f"{song['genre']} {song['mood']} {song['energy']} {song['valence']}".lower()

        if any(term in song_text for term in expanded_terms):
            results.append(song)

    log(f"Query: {query} | Expanded: {expanded_terms} | Results: {len(results)}")

    return results


def generate_explanation(query: str, song: Dict) -> str:
    """
    Simulated AI explanation (you can upgrade later with OpenAI API)
    """
    explanation = f"This matches your '{query}' because it is {song['mood']} and in the {song['genre']} genre."
    
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

    # MOOD
    if any(word in query for word in ["sad", "cry", "emotional"]):
        prefs["favorite_mood"] = "sad"
        prefs["target_valence"] = 0.2

    if any(word in query for word in ["happy", "fun", "upbeat"]):
        prefs["favorite_mood"] = "happy"
        prefs["target_valence"] = 0.9

    if "chill" in query or "study" in query or "relax" in query:
        prefs["favorite_mood"] = "chill"
        prefs["target_energy"] = 0.3
        prefs["target_acousticness"] = 0.7

    if "angry" in query:
        prefs["favorite_mood"] = "angry"
        prefs["target_energy"] = 0.95

    # GENRE
    if "rock" in query:
        prefs["favorite_genre"] = "rock"

    elif "pop" in query:
        prefs["favorite_genre"] = "pop"

    elif "indie" in query:
        prefs["favorite_genre"] = "indie"

    elif "edm" in query or "electronic" in query:
        prefs["favorite_genre"] = "electronic"

    elif "kpop" in query:
        prefs["favorite_genre"] = "kpop"

    elif "hiphop" in query or "rap" in query:
        prefs["favorite_genre"] = "hiphop"

    # ENERGY
    if "low-energy" in query or "calm" in query:
        prefs["target_energy"] = 0.2

    if "high energy" in query or "gym" in query:
        prefs["target_energy"] = 0.95

    # DANCE
    if "dance" in query:
        prefs["target_danceability"] = 0.95

    return prefs