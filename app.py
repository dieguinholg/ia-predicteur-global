
import streamlit as st
import json
from utils.api_football import *
from utils.api_news import *
from utils.value_bets import *
from utils.arbitrage import *
from utils.predictions import *
from utils.nlp import *


# Charger les concepts
with open("data/base_concepts.json", "r") as f:
    concepts = json.load(f)

# Analyse IA
st.set_page_config(layout="wide")
st.title("🔎 MOTEUR IA PRÉDICTIF GLOBAL & CONNECTÉ")
query = st.text_input("🧠 Tape une phrase, une intuition ou un sujet libre :")

if query:
    scores = nlp.get_similarity_scores(query, concepts)
    concept_names = list(concepts.keys())

    st.markdown("### 🧠 Résultats d'analyse IA :")
    for i, score in enumerate(scores):
        percent = int(score * 100)
        bg = "#fff000" if percent >= 80 else "#f0f0f0" if percent >= 60 else "#ffdddd"
        st.markdown(f"<div style='background-color:{bg}; padding:10px; border-radius:6px;'>"
                    f"<strong>{concept_names[i]}</strong> → {concepts[concept_names[i]]}<br>"
                    f"<em>Score de lien : {percent}%</em></div><br>", unsafe_allow_html=True)

    # Match PSG
    if "PSG" in query or "Paris SG" in query:
        st.markdown("### ⚽ Match du PSG :")
        data = api_football.get_match_info(85)
        st.json(data)

    # Actualité
    st.markdown("### 📰 Actualités liées :")
    news = api_news.get_news(query)
    for article in news.get("articles", [])[:3]:
        st.markdown(f"**[{article['title']}]({article['url']})**")
        st.caption(article["publishedAt"])

    # Value bet test (exemple)
    st.markdown("### 💰 Analyse Value Bet :")
    if value_bets.detect_value_bet(odds=2.0, probability=0.6):
        st.success("✅ Value Bet détecté (valeur positive)")
    else:
        st.warning("❌ Pas de value bet détecté")

    # Arbitrage test
    st.markdown("### ♻️ Analyse Arbitrage :")
    if arbitrage.detect_arbitrage(odds1=2.1, odds2=2.1):
        st.success("✅ Arbitrage possible entre les cotes")
    else:
        st.warning("❌ Aucun arbitrage détecté")

    # Générateur prédictif
    st.markdown("### 🔮 Prédiction IA :")
    st.info(predictions.generate_prediction(query))
