from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

documents = [
    Document(page_content="A balanced diet containing fruits, vegetables, whole grains, lean proteins, and healthy fats is essential for maintaining good health."),
    Document(page_content="Regular physical activity, such as walking, jogging, or cycling for at least 30 minutes a day, reduces the risk of heart disease and diabetes."),
    Document(page_content="Adequate sleep of seven to nine hours each night improves memory, concentration, immune function, and overall well-being."),
    Document(page_content="Drinking sufficient water throughout the day helps regulate body temperature, transport nutrients, and prevent dehydration."),
    Document(page_content="Mental health is just as important as physical health. Stress management techniques such as meditation, deep breathing, and exercise can improve emotional well-being."),
    Document(page_content="Vaccinations protect individuals from infectious diseases by helping the immune system recognize and fight harmful pathogens."),
    Document(page_content="Maintaining a healthy body weight through proper nutrition and regular exercise lowers the risk of obesity-related diseases."),
    Document(page_content="High blood pressure is often called the silent killer because it may not show symptoms while increasing the risk of heart attack and stroke."),
    Document(page_content="Diabetes is a chronic condition in which the body cannot properly regulate blood sugar levels due to insufficient insulin production or insulin resistance."),
    Document(page_content="Routine medical checkups and preventive screenings help detect diseases early, improving the chances of successful treatment.")
]

embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2-preview")
vector_store = FAISS.from_documents(
    embedding= embedding,
    documents=documents
)
similarity_retriever = vector_store.as_retriever(search_type = "similarity",search_kwargs = ({"k":5})) # simple similarity retriver

multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever = vector_store.as_retriever(search_kwargs = {"k":5}),
    llm = model
)

query = "How to stay healthy and active"

resul1 = similarity_retriever.invoke(query)
result2 = multi_query_retriever.invoke(query)

for docs in resul1:  # result from similarity search based retrival
    print(docs.page_content)

for docs in result2: # result from multi query retrieval 
    print(docs.page_content)

