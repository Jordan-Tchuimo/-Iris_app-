from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Sauvegarde du modèle KNN optimisé avec pickle
with open('knn_model.pkl', 'wb') as file:
    pickle.dump(best_knn, file)

# Charger le modèle
with open('knn_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
import streamlit as st
import requests

# Saisir les données d'entrée
sepal_length = st.number_input('Longueur du sépale', min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input('Largeur du sépale', min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input('Longueur du pétale', min_value=0.0, max_value=10.0, value=3.0)
petal_width = st.number_input('Largeur du pétale', min_value=0.0, max_value=10.0, value=1.0)

# Appeler l'API Flask
if st.button('Prédire'):
    response = requests.post('http://localhost:5000/predict', json={
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    })
    prediction = response.json()['prediction']
    st.write(f"La prédiction pour cette fleur est : {prediction}")
