import json
from backend.cache.redis_client import redis_client


SESSION_PREFIX = "session"
SESSION_EXPIRE = 86400  # 24 Hours


class SessionManager:

    @staticmethod
    def create_session(user_id: int, token: str):

        key = f"{SESSION_PREFIX}:{user_id}"

        redis_client.setex(
            key,
            SESSION_EXPIRE,
            json.dumps(
                {
                    "user_id": user_id,
                    "token": token
                }
            )
        )

    @staticmethod
    def get_session(user_id: int):

        key = f"{SESSION_PREFIX}:{user_id}"

        session = redis_client.get(key)

        if session:
            return json.loads(session)

        return None

    @staticmethod
    def delete_session(user_id: int):

        key = f"{SESSION_PREFIX}:{user_id}"

        redis_client.delete(key)

    @staticmethod
    def session_exists(user_id: int):

        key = f"{SESSION_PREFIX}:{user_id}"

        return redis_client.exists(key)

    @staticmethod
    def refresh_session(user_id: int):

        key = f"{SESSION_PREFIX}:{user_id}"

        redis_client.expire(
            key,
            SESSION_EXPIRE
        )