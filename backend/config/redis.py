import os
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username="default",      # Required for Upstash
    password=REDIS_PASSWORD,
    ssl=True,                # Required for Upstash
    decode_responses=True
)

def get_redis():
    return redis_client