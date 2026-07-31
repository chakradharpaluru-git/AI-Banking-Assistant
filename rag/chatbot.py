import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from rag.retriever import retrieve_documents
from rag.config import GROQ_API_KEY


# =====================================
# Load Environment Variables
# =====================================

load_dotenv()


# =====================================
# Initialize Groq LLM
# =====================================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    api_key=GROQ_API_KEY
)


# =====================================
# Prompt Template
# =====================================

prompt = ChatPromptTemplate.from_template(
"""
You are an AI Banking Assistant specialized in RBI policies.

Answer the question clearly using the provided context.

Rules:
- Explain the policy in simple language.
- Prefer definitions and main rules over minor details.
- Do not answer using unrelated sections.
- If the context does not contain the answer, say:
  "The information is not available in the provided banking documents."

Context:

{context}


Question:

{question}


Answer:
"""
)

# =====================================
# Chatbot Function
# =====================================

def ask_question(question):

    # 1. Retrieve relevant chunks
    documents = retrieve_documents(question)


    # 2. Convert documents into context

    context = "\n\n".join(
        [
            doc.page_content
            for doc in documents
        ]
    )


    # 3. Send context + question to LLM

    final_prompt = prompt.format(
        context=context,
        question=question
    )


    response = llm.invoke(final_prompt)


    # 4. Return answer

    return response.content



# =====================================
# Testing
# =====================================

if __name__ == "__main__":


    while True:

        question = input("\nAsk Banking Question: ")


        if question.lower() == "exit":
            break


        answer = ask_question(question)


        print("\nAI Banking Assistant:")
        print(answer)