import streamlit as st
import os
import sys



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) ## USE THIS CODE TO MOVE TO THE RELATIVE ROOT FILE

sys.path.append(BASE_DIR) ## USE THIS CODE TO MOVE TO THE RELATIVE ROOT FILE

from db.database import init_db

from core.services import DocumentServices # importing document services
init_db()

service = DocumentServices()

st.set_page_config(page_title="DocManager", layout="wide")

st.title("📁 Smart PDF Document Manager")

st.divider()

tabs = st.tabs(["Upload", "Search & View", "Analytics"])

with tabs[0]:
    ## logic for upload
    st.header("Upload PDF")
    
    uploaded_file = st.file_uploader("Upload PDF", type= ['pdf']) 
    tags = st.text_input("Tags (comma separated)")
    description = st.text_area("Description")
    lecture_date = st.date_input("Lecture Date (Optional)", value=None)

    if st.button("Upload"):
        if uploaded_file: # to check if uploaded file is there or not
            service.upload_document(uploaded_file, tags, description, lecture_date)
        else:
            st.error("Please upload the file")


with tabs[1]:
    # logic for search & view
    pass


with tabs[2]:
    # logic for analytics
    pass