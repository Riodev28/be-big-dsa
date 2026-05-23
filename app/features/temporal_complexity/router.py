from fastapi import APIRouter, Body, status
from . import TemporalComplexityService
from . import TemporalComplexityRequest
from ...shared.cache import CacheService
from ...shared.cache.client import make_client


router = APIRouter()

cache = CacheService(make_client())

service = TemporalComplexityService(cache)

@router.post("/temporal", status_code=status.HTTP_200_OK)
async def analyze(body: TemporalComplexityRequest):
    return service.analyze(body)
