from backend.cache.cache_service import CacheService


key = CacheService.create_key(
    "policy_rag",
    "what documents are required for kyc?"
)


deleted = CacheService.delete(key)


print("Deleted:", deleted)