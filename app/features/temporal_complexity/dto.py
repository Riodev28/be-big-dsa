from pydantic import BaseModel
from ..reports import TemporalAnalysisReport
from ..reports import TemporalAIReport


class TemporalComplexityResponseDTO(BaseModel):
    analysis: TemporalAnalysisReport
    ai: TemporalAIReport | None
