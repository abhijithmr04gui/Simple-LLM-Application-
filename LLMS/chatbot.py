from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate #used for single message prompt template
from langchain_core.prompts.chat import ChatPromptTemplate #used for chat prompt template
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


from dotenv import load_dotenv
import streamlit as st

load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

chat_history = [] # as llm does not know the previous conversation , we need to keep track of the conversation history and pass it to the model for context

while True:
    user_input = input("You : ")
    chat_history.append(SystemMessage(content = "You are a powerful AI assistant that is capable of answering any question and providing information on a wide range of topics."))
    chat_history.append(HumanMessage(content = user_input))
    if(user_input == "exit"):
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI :" , result) 
print(chat_history)