from pydantic import BaseModel
from ..reports import TemporalAnalysisReport

class TemporalComplexityResponseDTO(BaseModel):
    analysis: TemporalAnalysisReport
        