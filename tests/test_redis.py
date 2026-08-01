import os
import redis
from dotenv import load_dotenv

load_dotenv()

client = redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)

client.set("bank_name", "AI Banking Assistant")
print(client.get("bank_name"))