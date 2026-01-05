import streamlit as st
st.title("Text Input")
name = st.text_input("Enter Your Name")
comments = st.text_area("Enter Message")
st.write("**-: Output :-**")
if name:
    st.write(f"Hello, **{name}**")
if comments:
    st.write("-: Your Message :-")
    st.write(comments)
