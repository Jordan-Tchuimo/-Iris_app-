import streamlit as st
#EDA



#title/text
st.title("iris EDA App")
st.text("Built with streamlit")

#EDA
my_dataset = 'iris.csv'

#Fxn to Load Dataset

def explore_data(dataset):
  df = pd.read_csv(os.path.join(dataset))
  return df


if st.checkbox ("Preview Dataset"):
  data = explore_data(my_dataset)
  if st.button("Head"):
    st.write(data.head())


