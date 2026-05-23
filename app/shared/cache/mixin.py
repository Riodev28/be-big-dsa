from .service import CacheService
from ..ast.fingerprint import Fingerprint

class CacheMixin:
    cache_service: CacheService

    def process_cache(self, namespace: str, fingerprint: Fingerprint):
        """ Follow procediments to process cache. Made for reuse it in multiples services """
        
        key = self.cache_service.generate_cache_key(namespace, fingerprint)
        cached = self.cache_service.get_cache(key)
        parsed = self.cache_service.load_cache(cached) if cached else None
        return key, parsed