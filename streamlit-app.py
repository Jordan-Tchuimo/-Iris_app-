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
if gender == 'Male':
  st.text("Hello Guy")
if gender==
