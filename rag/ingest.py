# ==========================================================
# AI Banking Assistant
# Module 11 - RAG
# Step 6 - Create Embeddings & Vector Database
# ==========================================================

import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_chroma import Chroma

print("=" * 70)
print("CREATING VECTOR DATABASE")
print("=" * 70)

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCS_FOLDER = os.path.join(BASE_DIR, "docs")

VECTOR_DB = os.path.join(BASE_DIR, "rag", "vectorstore")

# ==========================================================
# Load PDF Documents
# ==========================================================

documents = []

for root, dirs, files in os.walk(DOCS_FOLDER):

    for file in files:

        if file.endswith(".pdf"):

            path = os.path.join(root, file)

            print(f"Loading : {file}")

            loader = PyPDFLoader(path)

            documents.extend(loader.load())

print("\nTotal Pages :", len(documents))

# ==========================================================
# Split Documents
# ==========================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print("Total Chunks :", len(chunks))

# ==========================================================
# Create Embeddings
# ==========================================================

print("Loading Embedding Model...")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


print("Embedding Model Loaded Successfully")
# ==========================================================
# Create Chroma Vector Store
# ==========================================================
print("Creating Chroma Vector Database...")


db = Chroma(
    collection_name="banking_documents",
    embedding_function=embeddings,
    persist_directory="rag/vectorstore"
)


db.add_documents(chunks)


print("Vector Database Created Successfully")
print(VECTOR_DB)

print("\n" + "=" * 70)
print("STEP 6 COMPLETED SUCCESSFULLY")
print("=" * 70)