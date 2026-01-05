
import streamlit as st
from datetime import date, time

st.title("Date, Time & File Uploader Demo")

exam_date = st.date_input("Select Exam Date:", value=date.today())
start_time = st.time_input("Exam Start Time:", value=time(9, 0))

uploaded_file = st.file_uploader("Upload CSV file with student marks", type=["pdf","py"])

st.write(f"Selected exam date: {exam_date}")
st.write(f"Exam start time: {start_time}")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type) 
