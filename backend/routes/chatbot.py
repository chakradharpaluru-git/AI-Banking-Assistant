from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.cache.cache_service import CacheService


router = APIRouter(
    prefix="/chatbot",
    tags=["Policy Chatbot"]
)


class ChatRequest(BaseModel):
    question: str


CACHE_EXPIRE = 86400   # 24 hours


@router.post("/chat")
def chatbot(request: ChatRequest):

    try:

        question = request.question.strip().lower()

        if not question:

            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )


        # ==========================
        # Redis Cache Key
        # ==========================

        cache_key = CacheService.create_key(
            "policy_rag",
            question
        )


        # ==========================
        # Check Redis
        # ==========================

        cached = CacheService.get(cache_key)


        if cached:

            return {

                "source": "redis_cache",

                "agent": "policy_rag_agent",

                "question": question,

                "response": cached

            }



        # ==========================
        # Lazy Load RAG Agent
        # ==========================

        from backend.agents.policy_rag_agent import policy_rag_agent


        answer = policy_rag_agent(
            question
        )



        # ==========================
        # Save Response in Redis
        # ==========================

        CacheService.set(
            cache_key,
            answer,
            CACHE_EXPIRE
        )


        return {

            "source": "policy_rag",

            "agent": "policy_rag_agent",

            "question": question,

            "response": answer

        }


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )