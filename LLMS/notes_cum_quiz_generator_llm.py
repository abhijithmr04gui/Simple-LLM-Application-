from langchain_google_genai import ChatGoogleGenerativeAI \
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model1 = ChatGoogleGenerativeAI(model ="gemini-2.5-flash")

model2 = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= "Generate a detailed Notes on the Topic \n {Topic}",
    input_variables=['Topic']
)

prompt2 = PromptTemplate(
    template= "Generate a set of  5 MCQ based on the Topic \n {text}",
    input_variables= ['text']
)

prompt3 = PromptTemplate(
    template= "Merge the provided notes and MCQ into a single document , \n notes-> {notes},quiz->{quiz}",
    input_variables=['notes','quiz']
)

