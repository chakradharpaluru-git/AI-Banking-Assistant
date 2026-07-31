import sys
import os


# Add project root to Python path

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)



from backend.agents.policy_rag_agent import retriever



docs = retriever.invoke(
    "KYC documents"
)



print("="*50)
print(
    "Documents Found:",
    len(docs)
)
print("="*50)



for i, doc in enumerate(docs):

    print("\nDOCUMENT", i+1)

    print(
        doc.page_content[:500]
    )

    print("-"*50)