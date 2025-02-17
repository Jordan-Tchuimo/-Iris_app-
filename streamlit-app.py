from flask import Flask, request, jsonify
import pickle
import numpy as np
import streamlit as st
import requests


app = Flask(__name__)

# Charger le modèle KNN sauvegardé
with open('knn_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données envoyées dans la requête POST
    data = request.get_json()

    # Extraire les caractéristiques (en supposant qu'elles soient envoyées sous forme de liste ou dictionnaire)
    features = np.array([data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]).reshape(1, -1)

    # Faire la prédiction avec le modèle
    prediction = model.predict(features)

    # Retourner la prédiction sous forme de réponse JSON
    return jsonify({'species': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

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



