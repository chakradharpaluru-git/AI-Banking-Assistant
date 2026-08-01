import sys
import os

# Add project root to Python path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from backend.cache.cache_service import CacheService


print("Clearing Redis cache...")

CacheService.clear()

print("Redis cache cleared successfully")