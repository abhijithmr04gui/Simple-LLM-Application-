from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt1 = PromptTemplate(
    template = "Give a joke on the Topic {Topic}",
    input_variables=['Topic']

)
prompt2 = PromptTemplate(
    template = "Now explain this joke also {text}",
    input_variables = ['text']
)
runnable_chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
result = runnable_chain.invoke({'Topic':'animals'})
print(result)