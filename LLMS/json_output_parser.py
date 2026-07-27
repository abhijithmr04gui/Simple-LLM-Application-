from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import JsonOutputParser


load_dotenv() 

parser = JsonOutputParser()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")

template1  = PromptTemplate(
    template="Give the name , age and gender of a fictional character in JSON Format{'First_Name'}",
    input_variables=['First_Name']
 )
prompt = template1.format()

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

print(type(final_result))

