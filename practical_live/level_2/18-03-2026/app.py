import streamlit as st

st.title("Streamlit demo")

# streamlit run app.py  ---===> used to run streamlit program in cmd

# Local system ip address
# 127.0.0.1
# 0.0.0.0
# localhost

st.write("This is streamlit demo app.")

name = st.text_input("Enter your name")
print(name)

st.write("End")

st.button("Press Enter", type="primary")

dob = st.date_input("Select Date of Birth")