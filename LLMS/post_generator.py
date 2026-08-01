from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
parser = StrOutputParser()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

Prompt1 = PromptTemplate(
    template = "Generate a Twitter Post on the Topic {Topic}",
    input_variables=['Topic']
)

Prompt2 = PromptTemplate(
    template = "Generate a Linkedin Post on the Topic {Topic}",
    input_variables=['Topic']
)

parallel_chain = RunnableParallel({       #Pass both the sequence chain in the form of dictionary
    'tweet' : RunnableSequence(Prompt1,model,parser),
    'post' : RunnableSequence(Prompt2,model,parser)
})

result = parallel_chain.invoke({'Topic':'AI'})

print(result)