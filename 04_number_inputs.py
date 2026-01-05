import streamlit as st
st.title("Number Input")
age = st.number_input("Enter Your Age", min_value=0, max_value=100, value=25)
rating = st.slider("Rate this session (1-10)",min_value=1,max_value=10, value=7)
st.write(f"Your Age : {age}")
st.write(f"You rated this workshop : {rating}/10")
