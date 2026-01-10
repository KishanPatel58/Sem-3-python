import streamlit as st 
weight = st.number_input("Weight (kg)",min_value=15)
height = st.number_input("Height (cm)",min_value=20)

if st.button("Click to calculate BMI"):
    BMI = weight / (height/100)**2
    st.write(f"BMI : {BMI}")
    if BMI<18.5:
        st.error("Underweight")
    elif(BMI>=18.5 and BMI<25):
        st.success("Normal")
    elif(BMI>=25 and BMI<30):
        st.warning("Overweight")
    else:
        st.error("Obese")
