import hashlib
import json

from backend.cache.redis_client import redis_client


class CacheService:

    @staticmethod
    def create_key(prefix: str, text: str):

        normalized = text.lower().strip()

        text_hash = hashlib.md5(
            normalized.encode("utf-8")
        ).hexdigest()

        return f"{prefix}:{text_hash}"

    @staticmethod
    def get(key):

        value = redis_client.get(key)

        if value:
            return json.loads(value)

        return None

    @staticmethod
    def set(key, value, expire=86400):

        redis_client.setex(
            key,
            expire,
            json.dumps(value)
        )

    @staticmethod
    def delete(key):

        redis_client.delete(key)

    @staticmethod
    def exists(key):

        return redis_client.exists(key)

    @staticmethod
    def clear():

        redis_client.flushdb()