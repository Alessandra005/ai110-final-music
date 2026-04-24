# 🧠 Model Card — AI Music Recommender System

## 📌 Model Overview

This system is a hybrid AI pipeline combining:

* Rule-based scoring
* Retrieval-Augmented Generation (RAG)
* Simulated explanation generation

It is designed to recommend songs based on natural language user input.

---

## 🎯 Intended Use

* Music recommendation based on mood, genre, and energy
* Educational demonstration of AI system design
* Portfolio project showcasing applied AI engineering

---

## ⚠️ Limitations

* Does not use a trained machine learning model
* Relies on keyword matching rather than deep NLP understanding
* May fail with complex or ambiguous queries
* Dataset size limits recommendation diversity

---

## ⚖️ Biases

* Dataset bias (certain genres/moods may be overrepresented)
* Keyword mapping bias (system prioritizes predefined categories)
* May not represent diverse musical tastes equally

---

## 🚨 Potential Misuse

* Over-reliance on recommendations without exploring new music
* Misinterpretation of system as fully intelligent AI

---

## 🛡️ Mitigations

* Confidence scores indicate uncertainty
* Transparent explanations show reasoning
* Logging helps track system decisions

---

## 🧪 Evaluation

* Retrieval test ensures relevant results are returned
* System logs behavior for debugging
* Confidence scores provide interpretability

Example:

> The system performs well on keyword-based queries but struggles with highly nuanced requests.
---
## Dataset

The system uses a custom dataset of **30 songs**, each annotated with:

- `title`  
- `artist`  
- `genre`  
- `mood`  
- `energy`  
- `tempo_bpm`  
- `valence`  
- `danceability`  
- `acousticness`

The dataset includes a mix of genres (indie, pop, hip-hop, kpop, reggaeton, rock, jazz, electronic, soul, latin pop, grunge) and moods (sad, chill, intense, happy, confident, energetic, nostalgic, dreamy, angry, bittersweet, etc.).

---

## 🏗️ Model Architecture

This system is not a neural model. Instead, it uses:

- **Keyword-based retrieval** (RAG)  
- **Rule-based scoring strategies**  
- **Template-based explanation generation**  
- **Confidence scoring** based on normalized recommendation scores  

This architecture prioritizes interpretability and modularity over predictive power.

---

## 🤖 Human + AI Collaboration

### Helpful AI Example:

AI assisted in designing the modular RAG pipeline and structuring the system into components (retrieval, scoring, explanation).

### Incorrect AI Example:

Initial retrieval logic was too strict and failed to return results for valid queries, requiring manual refinement.

---

## 🧠 Reflection

This project demonstrates the importance of:

* Breaking AI systems into modular components
* Testing reliability beyond surface-level outputs
* Balancing simplicity with functionality in system design
