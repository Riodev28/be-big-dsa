from ...shared.ast.fingerprint import Fingerprint
from ...shared.cache.service import CacheService
from .analyzer import TemporalComplexityAnalyzer
from .request import TemporalComplexityRequest
from .dto import TemporalComplexityResponseDTO
from ...shared.ast.value_objects.normalized_code import NormalizedCode
from ...shared.cache.mixin import CacheMixin
from ..reports import TemporalAnalysisReport


class TemporalComplexityService(CacheMixin):
    def __init__(self, cache_service: CacheService):
        self.cache_service = cache_service

    def analyze(self, payload: TemporalComplexityRequest):
        """Orchestrate payload. Analyze time complexity result"""

        normalized_code = NormalizedCode(payload.code)
        fingerprint = Fingerprint(normalized_code)

        key, cached = self.process_cache("temporal_complexity", fingerprint)

        if cached:
            return TemporalComplexityResponseDTO(
                analysis=TemporalAnalysisReport(**cached)
            )

        result = TemporalComplexityAnalyzer(normalized_code).analyze()
        self.cache_service.set_cache(key, result)

        return TemporalComplexityResponseDTO(analysis=result)
