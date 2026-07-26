from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)(
    
)

prompt1 = PromptTemplate(
    template="Write  a detailed report on {Topic}",
    input_variables=['Topic']
)
prompt2 = PromptTemplate(
    template= " Provide the 2 line summary of the review {Topic2}",
    input_variables=['Topic2']
)

answer1 = prompt1.invoke({'Topic':'solar system'})

result = model.invoke(answer1)

answer2 = prompt2.invoke({'Topic2':result.content})

result2 = model.invoke(answer2)

print(answer1)
print(result)

print(answer2)
print(result2)
    
