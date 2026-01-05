import streamlit as st
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="😁",
    layout="centered"
)
st.title("welcome to streamlit")
st.header("this is a header")
st.subheader("this is sub header")
st.text("this is text")
st.write("this is write")
st.markdown("this is markdown")
# display python
code_example = """
def add(a,b):
    return a+b
result = add(5,10)
print(result)
"""
st.code(code_example,language="python")
