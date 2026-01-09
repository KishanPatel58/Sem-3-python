import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Matplotlib + Streamlit Demo (plt version)")

# Sample data
x = np.arange(1, 11)
y = np.random.randint(50, 100, size=10)

# ----------------------------
# Line Chart
# ----------------------------
st.subheader("Line Chart (Matplotlib)")

#plt.figure(figsize=(6, 4))
plt.plot(x, y, marker="o")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Marks of 10 Students")

st.pyplot(plt)

# Clear the figure to avoid overlap
#plt.clf()

# ----------------------------
# Bar Chart
# ----------------------------
st.subheader("Bar Chart (Matplotlib)")

#plt.figure(figsize=(6, 4))
plt.bar(x, y)
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Marks Bar Chart")

st.pyplot(plt)

# Clear again
plt.clf() 
