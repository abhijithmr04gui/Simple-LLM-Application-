from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableLambda 
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

class Review(BaseModel):
    sentiment : Literal['Positive','Negative'] = Field(description='Give the sentiment of the review')

parser2 = PydanticOutputParser(pydantic_object=Review)

prompt1 = PromptTemplate(
    template= "Based on the review analyze classify whether it is positive or negative \n {review} \n {format_instructions}",
    input_variables= ['review'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)
prompt2 = PromptTemplate(
    template= "Write an appropriate response to the positive review {review}",
    input_variables=['review']
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to the Negative review {review}",
    input_variables= ['review']
)

classifier_chain = prompt1|model|parser2


branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive',prompt2|model|parser), 
    (lambda x:x.sentiment == 'Negative',prompt3|model|parser),
    RunnableLambda(lambda x: "Sentiment Not retrieved") # to convert a lambda function into a runnable so that it can be use as a chain 
)

final_chain = classifier_chain|branch_chain

result =  final_chain.invoke({'review':'This is a good laptop'})

print(result)