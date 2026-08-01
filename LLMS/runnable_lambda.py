from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda,RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Generate a Joke on the Topic {Topic}",
    input_variables= ['Topic']
)
initial_chain = RunnableSequence(prompt1,model,parser)

def countletters(text):
    count = 0
    for i in text :
        if(i.isalpha()):
            count = count+1
    return count 

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'letters' : RunnableLambda(countletters)
    })

final_chain = RunnableSequence(initial_chain,parallel_chain)

result = final_chain.invoke({'Topic':'Cricket'})

print(result)
