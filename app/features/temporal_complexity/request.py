from pydantic import BaseModel


class TemporalComplexityRequest(BaseModel):
    code: str
    explain_ai: bool = False
