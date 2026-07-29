from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

prompt = PromptTemplate(
    template = " Generate Five Intersting facts about {Topic}",
    input_variables= ['Topic']
)

parser = StrOutputParser()

chain = prompt | model | parser # chain

result = chain.invoke({'Topic':'India'})

print(result)

