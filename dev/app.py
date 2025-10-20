# app.py

import streamlit as st
import requests

# --- Configuration de la Page ---
st.set_page_config(
    page_title="Air Paradis - Analyse de Sentiment",
    page_icon="✈️",
    layout="centered"
)

# --- Contenu de l'Application ---

# Titre principal
st.title("✈️ Analyseur de Sentiment pour Air Paradise")

# Description
st.write(
    "Entrez un tweet ou un commentaire pour prédire si le sentiment est positif ou négatif."
    "Ceci est un prototype pour aider à anticiper les 'bad buzz'."
)

# Zone de saisie de texte pour l'utilisateur
user_input = st.text_area(
    "Écrivez le tweet à analyser ici :",
    "The flight was delayed for 3 hours, this is unacceptable!", # Exemple par défaut
    height=100
)

# Bouton pour lancer l'analyse
if st.button("Analyser le sentiment"):
    if user_input:
        # Affichage d'un message d'attente
        with st.spinner("Analyse en cours..."):
            try:
                # L'URL de notre API FastAPI (qui doit tourner en même temps)
                api_url = "http://127.0.0.1:8000/predict/"

                # Les données à envoyer à l'API (doivent correspondre au format de TweetInput)
                payload = {"text": user_input}

                # Appel de l'API avec une requête POST
                response = requests.post(api_url, json=payload)

                # Vérifier que la requête a réussi
                response.raise_for_status() 

                # Extraire le résultat
                result = response.json()
                sentiment = result["sentiment"]

                # Afficher le résultat de manière visuelle
                st.subheader("Résultat de l'analyse")
                if sentiment == "Négatif":
                    st.error(f"Sentiment prédit : **Négatif** 😡")
                else:
                    st.success(f"Sentiment prédit : **Positif** 😊")

                # --- BLOC AJOUTÉ : LES BOUTONS DE FEEDBACK ---
                st.write("Cette prédiction était-elle correcte ?")
                
                # On utilise des colonnes pour mettre les boutons côte à côte
                col1, col2 = st.columns(2)

                if col1.button("Prédiction Correcte 👍"):
                    # On affiche juste un message de remerciement
                    st.toast("Merci pour votre retour !")

                if col2.button("Prédiction Incorrecte 👎"):
                    # On envoie le feedback à notre endpoint /feedback/ de l'API
                    print("Sending BAD feedback...")
                    feedback_api_url = "http://127.0.0.1:8000/feedback/"
                    feedback_payload = {"text": user_input, "prediction": sentiment}
                    
                    try:
                        resp = requests.post(feedback_api_url, json=feedback_payload)
                        response.raise_for_status() 
                        print(f"Merci ! Le modèle sera amélioré grâce à votre retour. Response={resp}")
                        st.toast(f"Merci ! Le modèle sera amélioré grâce à votre retour. Response={resp}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"Impossible d'envoyer le feedback : {e}")
                    except Exception as e:
                        st.error(f"Une erreur est survenue lors de l'analyse : {e}")
                # --- FIN DU BLOC AJOUTÉ ---

            except requests.exceptions.RequestException as e:
                # Gérer les erreurs de connexion à l'API
                st.error(f"Erreur de connexion à l'API : {e}")
                st.warning("Assurez-vous que le serveur de l'API (FastAPI) est bien lancé.")
    else:
        st.warning("Veuillez entrer un texte à analyser.")