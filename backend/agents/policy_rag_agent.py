import os
import logging

from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(__name__)


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


VECTOR_DB_PATH = os.path.join(
    BASE_DIR,
    "rag",
    "vectorstore"
)


embeddings = None
vector_db = None
retriever = None
llm = None
prompt = None



def load_rag_components():

    global embeddings
    global vector_db
    global retriever
    global llm
    global prompt


    if retriever is None:

        logger.info("STEP 1: Loading RAG Components")


        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_chroma import Chroma
        from langchain_groq import ChatGroq
        from langchain_core.prompts import ChatPromptTemplate



        # ============================
        # Load Embedding Model
        # ============================

        logger.info(
            "STEP 2: Loading HuggingFace Embeddings"
        )


        embeddings = HuggingFaceEmbeddings(

            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"

        )


        logger.info(
            "STEP 3: Embeddings Loaded"
        )



        # ============================
        # Load ChromaDB
        # ============================

        logger.info(
            f"STEP 4: Loading ChromaDB from {VECTOR_DB_PATH}"
        )


        vector_db = Chroma(

            persist_directory=VECTOR_DB_PATH,

            embedding_function=embeddings

        )


        logger.info(
            "STEP 5: ChromaDB Loaded"
        )



        # ============================
        # Retriever
        # ============================

        retriever = vector_db.as_retriever(

            search_type="mmr",

            search_kwargs={

                "k":3,

                "fetch_k":10

            }

        )


        logger.info(
            "STEP 6: Retriever Loaded"
        )



        # ============================
        # Groq LLM
        # ============================

        logger.info(
            "STEP 7: Loading Groq Model"
        )


        groq_key = os.getenv(
            "GROQ_API_KEY"
        )


        if not groq_key:

            raise Exception(
                "GROQ_API_KEY missing"
            )


        llm = ChatGroq(

            model="llama-3.1-8b-instant",

            temperature=0.2,

            api_key=groq_key

        )


        logger.info(
            "STEP 8: Groq Loaded"
        )



        # ============================
        # Prompt
        # ============================

        prompt = ChatPromptTemplate.from_template(

"""
You are an RBI Banking Assistant.

Use ONLY the given RBI document context.

Answer banking questions clearly.

If information is unavailable say:

"I could not find this information in RBI documents."


Context:

{context}


Question:

{question}


Answer:
"""

        )


        logger.info(
            "STEP 9: RAG Components Loaded Successfully"
        )



    return retriever, llm, prompt





def policy_rag_agent(question: str):


    try:

        retriever, llm, prompt = load_rag_components()


        logger.info(
            f"Question: {question}"
        )



        # ============================
        # Retrieve Documents
        # ============================

        logger.info(
            "STEP 10: Searching ChromaDB"
        )


        docs = retriever.invoke(
            question
        )


        logger.info(
            f"STEP 11: Documents Found {len(docs)}"
        )



        if not docs:

            return (
                "I could not find this information in RBI documents."
            )



        context = "\n\n".join(

            [
                doc.page_content
                for doc in docs
            ]

        )



        # ============================
        # Generate Answer
        # ============================

        logger.info(
            "STEP 12: Calling Groq"
        )


        messages = prompt.format_messages(

            context=context,

            question=question

        )


        response = llm.invoke(
            messages
        )


        logger.info(
            "STEP 13: Answer Generated"
        )


        return response.content



    except Exception as e:


        logger.error(
            f"RAG ERROR: {e}"
        )


        return (
            "Unable to generate RBI policy answer."
        )