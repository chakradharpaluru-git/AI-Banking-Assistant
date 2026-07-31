from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# =====================================
# Load Embedding Model
# =====================================

print("Loading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded")


# =====================================
# Load Chroma Vector Database
# =====================================

print("Loading Vector Database...")


db = Chroma(
    collection_name="banking_documents",
    persist_directory="rag/vectorstore",
    embedding_function=embeddings
)


print("Vector Database Loaded")


# =====================================
# Create Retriever
# =====================================

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)


# =====================================
# Retrieve Documents Function
# =====================================

def retrieve_documents(question):

    documents = retriever.invoke(question)

    return documents



# =====================================
# Testing Retriever
# =====================================

if __name__ == "__main__":


    question = "What documents are needed for KYC?"


    print("\nQuestion:")
    print(question)


    results = retrieve_documents(question)


    print("\nRetrieved Chunks:")
    

    for index, doc in enumerate(results):

        print("\n==============================")
        print("Chunk:", index + 1)

        print("\nContent:")
        print(doc.page_content)


        print("\nMetadata:")
        print(doc.metadata)