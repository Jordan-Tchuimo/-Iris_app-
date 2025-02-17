import streamlit as st

#title/text
st.title("Iris EDA App")
st.text("Built with streamlit")

#Headers and subheader
st.header("EDA App")
st.subheader("Iris Dataset")


#Checkbox
if st.checkbox("Show Dataset"):
  st.text("Showing Dataset")

#Radio Buttons
gender = st.radio("what is your gender?",("Male","female"))
if gender=='Male':
  st.text("Hello Guy")


#Selection
occupation = st.selectbox("Occupation",("Programmer","Data scientist", "Doctor"))

#Sliders
age = st.slider("Your age",1,99)

#Buttons
if st.button("About Us"):
  st.text("Hello Us")

#Write
st.write("Hello world")

#Images
from PIL import 
import os.datetime
st.image(Image.open(os.path.join('Iris_sectosa.jpg')))

#Dates
st.date_input("Today date", datetime.datetime.now())

