from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash")

schemas = [
    ResponseSchema(name="fact_1", description="First fact"),
    ResponseSchema(name="fact_2", description="Second fact"),
    ResponseSchema(name="fact_3", description="Third fact"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)

prompt = PromptTemplate(
    template="""
Give me 3 facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)