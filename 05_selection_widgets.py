import streamlit as st

st.title("Selection Widgets Demo")

course = st.selectbox("Select Course:",["DAA", "CN", "TE-I", "EEF"])

preferred_days = st.multiselect(
    "Preferred Days for Extra Lectures",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
)

delivery_mode = st.radio(  "Preferred Delivery Mode:",
    ["Offline", "Online", "Hybrid"]
)

subscribe = st.checkbox("Subscribe to course updates?") #value=True

st.write("---")
st.write(f"**Course:** {course}")
st.write(f"**Preferred Days:** {', '.join(preferred_days) if preferred_days else 'None'}")
st.write(f"**Delivery Mode:** {delivery_mode}")
st.write(f"**Subscribed:** {'Yes' if subscribe else 'No'}") 
