from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.header("Gemini llm App")

input = st.text_input("Enter your prompt:")

if st.button("Summarize:") :
    result = ChatGoogleGenerativeAI(model = "gemini-2.5-flash").invoke(input)
