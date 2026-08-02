from langchain_community.document_loaders  import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")    

loader  = TextLoader('dummy.txt',encoding='utf-8')
docs = loader.load()

prompt1 = PromptTemplate(
    template= "Summarize the following text {Text}",
    input_variables = ['Text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser)

result = chain.invoke({'Text':docs[0].page_content})

print(result)