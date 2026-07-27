from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import Field,Optional
from typing import Literal
load_dotenv()

model = ChatGoogleGenerativeAI(model = "flash-2.5-gemini")

class Person(model):
    name:str = Field(description = "Enter the name of the Person")
    age:int = Field( gt = 18,description ="Enter the age of the Person" )
    gender : Literal['Male','Female'] = Field(description = "Enter the gender of the Person either male or female")

parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = "Enter the name of an {Place} Person",
    input_variables = ['Place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'Place':'Indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)




