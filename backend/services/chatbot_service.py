from backend.cache.cache_service import CacheService


CACHE_EXPIRE_TIME = 86400  # 24 hours


def generate_answer(question: str) -> str:
    """
    Current chatbot logic.
    Replace this function later with your RAG pipeline.
    """

    question = question.lower()

    if "loan" in question:
        return "Our bank offers personal, home, education, and business loans."

    elif "credit" in question:
        return "A higher credit score improves your chances of loan approval."

    elif "fraud" in question:
        return "Please block your card immediately and contact customer support."

    elif "account" in question:
        return "You can manage your account using the mobile banking application."

    else:
        return "I'm your AI Banking Assistant. Please ask a banking-related question."


def chat_response(question: str):
    """
    Chatbot with Redis cache.
    """

    cache_key = CacheService.create_key(
        "chatbot",
        question
    )

    cached_answer = CacheService.get(cache_key)

    if cached_answer:

        return {
            "source": "redis_cache",
            "answer": cached_answer
        }

    answer = generate_answer(question)

    CacheService.set(
        cache_key,
        answer,
        CACHE_EXPIRE_TIME
    )

    return {
        "source": "chatbot",
        "answer": answer
    }