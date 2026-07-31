import json

from backend.cache.redis_client import redis_client


MEMORY_PREFIX = "conversation"
MEMORY_EXPIRE = 86400   # 24 Hours


class ConversationMemory:

    @staticmethod
    def _key(session_id: str):

        return f"{MEMORY_PREFIX}:{session_id}"

    @staticmethod
    def get_history(session_id: str):

        data = redis_client.get(
            ConversationMemory._key(session_id)
        )

        if data:
            return json.loads(data)

        return []

    @staticmethod
    def save_history(session_id: str, history):

        redis_client.setex(
            ConversationMemory._key(session_id),
            MEMORY_EXPIRE,
            json.dumps(history)
        )

    @staticmethod
    def add_message(
        session_id: str,
        role: str,
        message: str
    ):

        history = ConversationMemory.get_history(
            session_id
        )

        history.append(
            {
                "role": role,
                "message": message
            }
        )

        ConversationMemory.save_history(
            session_id,
            history
        )

    @staticmethod
    def clear(session_id: str):

        redis_client.delete(
            ConversationMemory._key(session_id)
        )