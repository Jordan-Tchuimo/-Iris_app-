import streamlit as st
import requests

# Créer l'interface utilisateur
st.title("Prédiction de l'Espèce d'Iris")

# Formulaire pour saisir les caractéristiques de l'iris
sepal_length = st.number_input('Longueur du sépale (cm)', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Largeur du sépale (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Longueur du pétale (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Largeur du pétale (cm)', min_value=0.0, max_value=10.0, step=0.1)

# Créer un bouton pour envoyer la requête
if st.button('Faire une Prédiction'):
    # Organiser les données dans un dictionnaire
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    # Faire une requête POST à l'API Flask
    response = requests.post("http://127.0.0.1:5000/predict", json=data)

    # Afficher la prédiction
    if response.status_code == 200:
        prediction = response.json()['species']
        st.write(f"La prédiction est : {prediction}")
    else:
        st.write("Erreur dans la requête")



