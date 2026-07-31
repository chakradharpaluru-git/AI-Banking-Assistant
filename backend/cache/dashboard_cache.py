import json

from backend.cache.redis_client import redis_client

CACHE_TIME = 3600  # 1 Hour


class DashboardCache:

    @staticmethod
    def key(user_id: int):

        return f"dashboard:{user_id}"

    @staticmethod
    def get(user_id: int):

        data = redis_client.get(
            DashboardCache.key(user_id)
        )

        if data:
            return json.loads(data)

        return None

    @staticmethod
    def set(user_id: int, dashboard_data: dict):

        redis_client.setex(
            DashboardCache.key(user_id),
            CACHE_TIME,
            json.dumps(dashboard_data)
        )

    @staticmethod
    def delete(user_id: int):

        redis_client.delete(
            DashboardCache.key(user_id)
        )

    @staticmethod
    def refresh(user_id: int, dashboard_data: dict):

        DashboardCache.delete(user_id)
        DashboardCache.set(user_id, dashboard_data)