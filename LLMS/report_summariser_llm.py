from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="Give me a detailed report on the Topic {Topic}",
    input_variables= ['Topic']
)

prompt2 = PromptTemplate(
    template="Summarize the report in Five lines from the text {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model| parser | prompt2 | model | parser

result = chain.invoke({'Topic':'Education System in India '})

#print(result)
chain.get_graph().print(ascii)
