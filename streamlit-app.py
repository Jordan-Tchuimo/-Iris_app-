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
my_dataset = 'Iris.csv'

#Fxn to Load Dataset

def explore_data(dataset):
  df = pd.read_csv("Iris.csv")  # Example, check this
  return df



if st.checkbox ("Preview Dataset"):
  data = explore_data(my_dataset)
  if st.button("Head"):
    st.write(data.head())
  elif st.button("Tail"):
    st.write(data.tail())
  else:
    st.write(data.head(2))

#Show entire dataset
if st.checkbox("Show All Dataset"):
  #st.write(data)
  st.dataframe(data)

#Show Column Name
if st.checkbox("Show Column Names"):
  st.write(data.columns)


#Show Dimensions
data_dim= st.radio("What Dimensions Do you want to see?",("Rows","Columns","All"))
if data_dim == 'Rows':
  st.text("Showing Rows")
  st.write(data.shape[0])
elif data_dim == 'Columns':
  st.text("Showing Columns")
  st.write(data.shape[1])
else:
  st.text("Showing Shape of Dataset")
  st.write(data.shape)


#Sumary
if st.checkbox("Show Sumary of Dataset"):
  st.write(data.describe())

#Select A Columns
col_option = st.selectbox("Select Column",("sepallength","sepalwidth","petallength","petalwidth","species"))
if col_option == 'sepalwidth':
  st.write(data['sepalwidth'])
elif col_option == 'sepallength':
  st.write(data['sepallength'])
elif col_option == 'petalwidth':
  st.write(data['petalwidth'])
elif col_option == 'petallength':
  st.write(data['petallength'])
elif col_option == 'species':
  st.write(data['species'])
else:
  st.write("Select Column")

#Plot
if st.checkbox("Show Bar Plot with Matplotlib"):
  st.write(data.plot(kind='bar'))
  st.pyplot()

#Correlation
if st.checkbox("Show Correlation Plot with Matplotlib"):
  plt.matshow(data.corr()))
  st.pyplot()

#Correlation
if st.checkbox("Show Correlation Plot with Seaborn"):
  st.write(sns.heatmap(data.corr()))
  st.pyplot()

#Group
if st.checkbox("Show Bar Chart Plot"):
  v_group = data.groupby('species)
  st.bar_chart(v_group)

#Group
if st.checkbox("Show Line Plot"):
  v_group = data.groupby('species)
  st.Line_chart(data)

#Group
if st.checkbox("Show Area Chart Plot"):
  v_group = data.groupby('species)
  st.area_chart(v_group)


#Images

