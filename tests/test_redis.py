from backend.cache.redis_client import redis_client

redis_client.set("bank_name", "AI Banking Assistant")

print(redis_client.get("bank_name"))