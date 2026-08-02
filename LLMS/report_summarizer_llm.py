from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda,RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Generate a report on the Topic {Topic}",
    input_variables= ['Topic']
)

prompt2 = PromptTemplate(
    template = "Summarize the following text {Text} ",
    input_variables=['Text']
)

def count_word(text):
    count = len(text.split())
    return count 

initial_chain = RunnableSequence(prompt1,model,parser)

branch = RunnableBranch(
    (RunnableLambda(lambda x : count_word(x)>5000), RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough() # default 
)

final_chain = RunnableSequence(initial_chain,branch)

result = final_chain.invoke({
'Topic':'Cricket'
})
print(result)


    
