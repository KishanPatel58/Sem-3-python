
import streamlit as st
import time

st.title("Status Elements Demo")

st.success("This is a success message.")
st.warning("This is a warning message.")
st.error("This is an error message.")
st.info("Useful information can go here.")

st.write("---")
st.subheader("Progress & Spinner Example")

if st.button("Start Long Task"):
    progress = st.progress(0)
    with st.spinner("Processing..."):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i + 1)
    st.success("Task completed!") 
