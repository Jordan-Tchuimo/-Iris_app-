
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Charger le jeu de données Iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Titre de l'application
st.title('Analyse du jeu de données Iris')

# Afficher les premières lignes du jeu de données
st.subheader('Voici les premières lignes du jeu de données Iris:')
st.write(df.head())

# Visualisation interactive avec Seaborn
st.subheader('Visualisation des relations entre les variables')
sns.pairplot(df, hue="species")
st.pyplot()

# Afficher des statistiques descriptives
st.subheader('Statistiques descriptives du jeu de données Iris:')
st.write(df.describe())

