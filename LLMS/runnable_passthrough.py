from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence , RunnablePassthrough,RunnableParallel
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

joke_gen_chain = RunnableSequence(prompt1,model,parser)


parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough.invoke({'Topic':'Work'}),
    'explanation' :RunnableSequence.invoke(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'Topic':'Cricket'})

print(result)