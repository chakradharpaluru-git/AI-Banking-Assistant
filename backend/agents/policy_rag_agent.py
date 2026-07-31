import os
import logging

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate


# =====================================================
# ENV
# =====================================================

load_dotenv()


logging.basicConfig(
    level=logging.INFO
)


logger = logging.getLogger(__name__)



# =====================================================
# PROJECT PATH
# =====================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)



# Your vector database location

VECTOR_DB_PATH = os.path.join(

    BASE_DIR,

    "rag",

    "vectorstore"

)



logger.info(
    f"Loading Vector Database : {VECTOR_DB_PATH}"
)



# =====================================================
# EMBEDDING MODEL
# =====================================================


embeddings = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"

)



# =====================================================
# CHROMA VECTOR DATABASE
# =====================================================


vector_db = Chroma(

    persist_directory=VECTOR_DB_PATH,

    embedding_function=embeddings

)



logger.info(
    "Chroma Database Loaded Successfully"
)



# =====================================================
# RETRIEVER
# =====================================================


retriever = vector_db.as_retriever(

    search_type="mmr",

    search_kwargs={

        "k":3,

        "fetch_k":10

    }

)



# =====================================================
# GROQ LLM
# =====================================================


llm = ChatGroq(

    model="llama-3.1-8b-instant",

    temperature=0.2,

    api_key=os.getenv(
        "GROQ_API_KEY"
    )

)



# =====================================================
# PROMPT
# =====================================================


prompt = ChatPromptTemplate.from_template(

"""
You are an RBI Banking Assistant.

Your job is to answer questions related to Indian banking.

Use ONLY the given RBI document context.

Rules:

1. Give answers for normal bank customers.

2. Ignore documents related to:
- Foreign Portfolio Investors (FPI)
- SEBI investors
- Stock market participants

unless the user specifically asks about them.

3. Prefer information related to:

- Customer KYC
- Bank accounts
- Loans
- UPI
- Digital banking
- RBI rules


4. If information is not available:

Say:

"I could not find this information in RBI documents."


Keep the answer simple and clear.


Context:

{context}


Question:

{question}


Answer:

"""

)



# =====================================================
# POLICY RAG AGENT
# =====================================================


def policy_rag_agent(question:str):


    try:


        logger.info(
            f"User Question : {question}"
        )



        # Retrieve documents

        docs = retriever.invoke(
            question
        )



        logger.info(
            f"Documents Retrieved : {len(docs)}"
        )



        if not docs:


            return (
                "I could not find this information "
                "in RBI documents."
            )



        context = "\n\n".join(

            [

                doc.page_content

                for doc in docs

            ]

        )



        messages = prompt.format_messages(

            context=context,

            question=question

        )



        response = llm.invoke(
            messages
        )



        return response.content



    except Exception as e:


        logger.error(
            f"RAG Error : {e}"
        )


        return (
            "Unable to generate RBI policy answer."
        )
