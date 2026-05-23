import redis
from ...core.config import settings


class Cache:
    """Adapter over Cache system that exposes a minimal get/set interface.

    Decouples the rest of the codebase from cache database directly,
    so swapping the backing store only requires changing this class.
    """

    def __init__(self):
        self.cache = redis.Redis.from_url(settings.redis_url, decode_responses=True)

    def get(self, key: str):
        return self.cache.get(name=key)

    def set(self, cache_key: str, value: str, ex_ttl: int = 3600):
        self.cache.set(name=cache_key, value=value, ex=ex_ttl)

    @staticmethod
    def from_url() -> "Cache":
        return Cache()
