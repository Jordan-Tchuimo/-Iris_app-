import streamlit as st
#EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from PIL import Image


#title/text
st.title("Iris EDA App")
st.text("Built with streamlit")

#EDA
my dataset = 'Iris.csv'

#Fxn to Load Dataset

def explore_data(dataset):
  df = pd.read_csv(os.path.join(dataset))
  return df


if st.checkbox ("Preview Dataset"):
  data = explore_data(my dataser)
  if st.button("Head"):
    st.write(data.head())


