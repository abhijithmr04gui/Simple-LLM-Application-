from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

model  = GoogleGenerativeAI(model = "gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="Write  a detailed report on {Topic}",
    input_variables=['Topic']
)
prompt2 = PromptTemplate(
    template= " Provide the 2 line summary of the review {Topic2}",
    input_variables=['Topic2']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | RunnableLambda(lambda x: {"Topic2": x})| prompt2 | model | parser

output = chain.invoke({'Topic':'Solar System'})

print(output)