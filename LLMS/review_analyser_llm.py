from langchain_google_genai import ChatGoogleGemini
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import TypedDict,Annotated

load_dotenv()

model = ChatGoogleGemini(model ='gemini-2.5-flash')

class Review(TypedDict):
    summary : Annotated[str, "The summary of the Review"]
    product : Annotated[str,"The product review if mentioned in the review"]
    sentiment :Annotated[str,"The sentiment of the review either positive, negative or neutral"]  
structured_review_model = model.with_structured_output(Review)  # kinda inbuilt prompt template for structured output
review = structured_review_model.invoke("This book exceeded my expectations. The characters felt real, the plot was engaging, and I couldn't put it down. I finished it in two days and would definitely " \
"recommend it to anyone who enjoys mystery novels.")

print(review)