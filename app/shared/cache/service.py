from typing import Any, Mapping
from dataclasses import asdict, is_dataclass
import json

from app.shared.cache.cache import Cache
from app.shared.ast.fingerprint import Fingerprint

class CacheService():
    def __init__(self, client: Cache):
        self.client: Cache = client
    
    def get_cache(self, key: str) -> str | None:
        """ Get from client cache if exists"""
        return self.client.get(key)
    
    
    def set_cache(
        self,
        cache_key: str,
        value: Mapping[str, Any] | Any,
        ex_ttl: int = 3600
    ) -> None:
        """ Store cache on database.
            - Format: "{key: serialized value}"
            - Example: "{"time_complexity": "O(n\u00b3)", "max_loop_depth": 3, "recursive": false}"
        """
        serialized = self._serialize(value)
        self.client.set(cache_key, json.dumps(serialized), ex_ttl=ex_ttl)
    
    
    def load_cache(self, cached: str) -> dict[str, Any]:
        """ Load cache in json """
        return json.loads(cached)
    
    
    def generate_cache_key(self, namespace: str, fingerprint: Fingerprint) -> str:
        """ Generate a unique cache key """
        
        return f"{namespace}:{fingerprint.digest()}"
    
    
    @staticmethod
    def _serialize(value: Any) -> Any:
        """ Serialize any value """
        if is_dataclass(value):
            return asdict(value)

        return value