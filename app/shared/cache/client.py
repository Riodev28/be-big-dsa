from .cache import Cache


def make_client() -> Cache:
    """Create a new instance of cache client"""
    return Cache.from_url()
