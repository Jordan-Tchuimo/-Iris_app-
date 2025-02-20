
import streamlit as st
import requests
import numpy as np 
import pandas as pd
import joblib
# Créer l'interface utilisateur
st.title("Prédiction de l'Espèce d'Iris")

# Formulaire pour saisir les caractéristiques de l'iris
sepal_length = st.number_input('Longueur du sépale (cm)', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Largeur du sépale (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Longueur du pétale (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Largeur du pétale (cm)', min_value=0.0, max_value=10.0, step=0.1)

# Créer un bouton pour envoyer la requête
if st.button('Faire une Prédiction'):
    # Préparation des données d'entrée
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    X = pd.DataFrame(features, columns=["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"])
    scaler = joblib.load("mon_scaler.pkl")
    model = joblib.load("mon_model2.pkl")
    X_transform = scaler.transform(X)
    reponse = model.predict(X_transform)
    prediction = reponse[0]
    
    
    # Affichage du résultat
    st.write("Ta fleur est: ", prediction)



