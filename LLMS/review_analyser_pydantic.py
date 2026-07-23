from langchain_google_genai import ChatGoogleGemini
from dotenv import load_dotenv
from typing import Literal
from pydantic import BaseModel ,Field,Optional

load_dotenv()

model = ChatGoogleGemini(model ='gemini-2.5-flash')

class Review(BaseModel):
    summary : str = Field(description = "Summarize the Review in short")
    author : str = Field(description = "Mention the Name of the person who wrote the review")
    sentiment : Literal["pos","neg"] = Field(description= "Mention the sentiment of the review whether positive or negative")
    pros : Optional[list[str]] = Field(description= "Write the pros of review")

    structured_model = model.with_structured_output(Review)

    result = structured_model.invoke("This book exceeded my expectations. The characters felt real, the plot was engaging, and I couldn't put it down. I finished it in two days and would definitely " \
"recommend it to anyone who enjoys mystery novels.")
    
    print(result)