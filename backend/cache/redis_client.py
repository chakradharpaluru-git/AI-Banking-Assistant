import os
import redis
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = int(os.getenv("REDIS_DB", 0))


# Create Redis Client
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=REDIS_DB,
    decode_responses=True,
    ssl=True
)


def get_redis():
    """
    Returns the shared Redis client.
    """
    return redis_client


def check_redis():

    try:
        redis_client.ping()
        print("✅ Redis Connected Successfully")
        return True

    except Exception as e:
        print("❌ Redis Connection Failed")
        print(e)
        return False