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


        logger.info(
            "Loading RAG Components..."
        )


        from langchain_huggingface import HuggingFaceEmbeddings

        from langchain_chroma import Chroma

        from langchain_groq import ChatGroq

        from langchain_core.prompts import ChatPromptTemplate



        embeddings = HuggingFaceEmbeddings(

            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"

        )



        vector_db = Chroma(

            persist_directory=VECTOR_DB_PATH,

            embedding_function=embeddings

        )



        retriever = vector_db.as_retriever(

            search_type="mmr",

            search_kwargs={

                "k":3,

                "fetch_k":10

            }

        )



        llm = ChatGroq(

            model="llama-3.1-8b-instant",

            temperature=0.2,

            api_key=os.getenv(
                "GROQ_API_KEY"
            )

        )



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
            "RAG Components Loaded"
        )



    return retriever, llm, prompt





def policy_rag_agent(question: str):


    try:


        retriever, llm, prompt = load_rag_components()



        logger.info(
            f"Question: {question}"
        )



        docs = retriever.invoke(
            question
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
            f"RAG Error: {e}"
        )


        return (
            "Unable to generate RBI policy answer."
        )