from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="Large Language Models (LLMs) are neural networks trained on massive text datasets to understand and generate human-like language."),
    
    Document(page_content="Retrieval-Augmented Generation (RAG) improves LLM responses by retrieving relevant information from external knowledge sources before generating an answer."),
    
    Document(page_content="Embeddings convert text into high-dimensional vectors so that semantically similar documents are located close to each other in vector space."),
    
    Document(page_content="Vector databases such as Chroma, FAISS, and Pinecone store embeddings and enable efficient similarity search for LLM applications."),
    
    Document(page_content="Prompt engineering is the process of designing effective prompts to guide an LLM toward producing accurate and relevant responses."),
    
    Document(page_content="LangChain provides tools for building LLM-powered applications, including document loaders, vector stores, retrievers, and chains.")
    ]

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

vector_store = FAISS.from_documents(
    documents= documents,
    embedding=embeddings
)
query = "Define What is an LLM "

retriver = vector_store.as_retriever(
    search_type  = "mmr",
    search_kwargs = {"k":3,"lambda_mult" : 1} # 1 - minimum diversity works like normal similarity search  , if lamda_mult = 0 - maximum diversity
)

result = retriver.invoke(query)

for doc in result:
    print(doc.page_content)