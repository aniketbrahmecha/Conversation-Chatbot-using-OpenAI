from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()


def get_response(query):
    llm_model = OpenAI(
        temperature=0.7,openai_api_key =os.environ["OPENAI_API_KEY"] 
    )
    response = llm_model(query)
    return response
    

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat") 

input=st.text_input("Input: ",key="input")
response=get_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)