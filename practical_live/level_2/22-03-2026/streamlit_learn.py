# streamlit run streamlit_learn.py
import streamlit as st
# st.write("Hello World")

st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="💥🚀",
    #layout = "wide"
    layout= "centered"
)

## Equivalent to --->> <h1>
st.title("Ultimate Data Science Class")

## Equivalent to --->> <h3>
st.subheader("Level 1")

## Equivalent to --->> <p>
st.write("This is the Batch 2 of ultimate data science boot camp")

# tabs
tab1, tab2, tab3 = st.tabs(["Home", "Dashboard", "Settings"])

with tab1:
    st.write("Welcome to the Home Tab")
    

    col1, col2, col3=st.columns(3)

    with col1:
        st.write("Left Section (Home)!")
        st.button("Click left Section Button",type="primary")

    with col2:
        st.write("Centered Section (Home)!")
        st.button("Click Centered Section Button", type="secondary")

    with col3:
        st.write("Right Section (Home)!")
        st.button("Click right Section Button", type="tertiary")

with tab2:
    st.write("Welcome to the Dashboard Tab")


with tab3:
    st.write("Welcome to the Settings Tab")

st.divider()
st.subheader("Level 2")
# container
with st.container(height = 200, border = True):
    for i in range(100):
        st.write(f"Hello {i}")

st.subheader("Level 2 - Widgets")
st.divider()
if st.button("Say Hello", type="primary") :
    st.write("Hello there!! You said hello")

st.link_button("Streamlit Widget Page Redirect", url= "https://docs.streamlit.io/develop/api-reference/widgets")

a=0
print(a)
name = st.text_input("Enter Name")
st.write(f"Hello {name.capitalize()}!")

count =0
if st.button("Click here to add 1 to the count"):
    count+=1
    st.write(f"Hello there!, the current count value is {count}")

u_name = st.text_input("Username")
p_u_name = st.text_input("Password", type="password")

st.text_area("Tell us about yourself ", height=200)

# select a date
st.subheader("level 4 - Dates")

import datetime
today = datetime.date.today()

picked_Date =st.date_input("Pick a date", today)
st.write(picked_Date)

st.divider()

## upload a file
from io import StringIO
uploaded_file = st.file_uploader("Upload a csv", type=["csv", "txt"])
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data=stringio.read()

    st.write("File Contents")

    #st.write(f"{uploaded_file}")
    st.code(string_data, language="text")
    st.write("File Uploaded Successfully")
    st.success("File Uploaded!!")

st.warning("File loading Warning!!!")
st.error("Error")
st.info("Here has useful tips")


## creating a counter
st.divider()
if 'count'not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count+=1
st.write(st.session_state.count)


## creating headers 
st.title("Main Title") ## Larger
st.header("Section Header") ## Medium
st.subheader("Sub section") ##  small

# use st.markdown()
st.markdown("We use a markdown here")

## writing html code in the markdown
st.markdown("<h1 style = 'color: blue; '>Custom Html developed </h1>", unsafe_allow_html=True)

## importing dataframe using pandas

import pandas as pd
import numpy as np

df =pd.DataFrame(np.random.randn(10,2) , columns=["A", "B"])
st.write("Streamlit data frame visualisation")
st.dataframe(df)
# adding barchart
st.write("Streamlit dataframe barchart")
st.bar_chart(df)

### image 
st.image(r"C:\Users\Alfred\Downloads\new sanlam.jpg", caption="my image Upload", width=400)


## adding a progress bar
import time

bar = st.progress(0)
for percent in range(100):
    time.sleep(0.1) ## to make it load slowly for me to see
    bar.progress(percent +1)


st.divider()

# downloading a file on streamlit
text_to_Save = "1,2,3,4,5"
st.download_button(
    label="Download text file",
    data=text_to_Save,
    file_name="dummy_file.txt",
    mime="text/plain"
)
