
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

documents  = [
    Document(page_content = "Langchain is a very important tool in the world of GENAI"),
    Document(page_content = "Langraph is used to make AI Agents")
]

embedding_model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2-preview")

vector_STORE = Chroma(
    documents = documents,
    embedding_function = embedding_model,
    collection_name = "my_collection"
)

retriever = vector_STORE.as_retriever( search_kwargs ={"k": 2})


query = "What is the use of Langraph"

result_2 = vector_STORE.similarity_search(query,k=2) # basic 

result = retriever.invoke(query)  

for i in result:
    print(i.page_content)