import streamlit as st
import requests

# Define the FastAPI endpoint
api_url = "http://127.0.0.1:8000/answer"

st.title("AI Assistant")
question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question:
        response = requests.get(api_url, params={"question": question})
        if response.status_code == 200:
            st.success(response.json()["answer"])
        else:
            st.error("Error: Unable to get a response.")
    else:
        st.warning("Please enter a question.")
