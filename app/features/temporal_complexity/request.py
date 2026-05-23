from pydantic import BaseModel


class TemporalComplexityRequest(BaseModel):
    code: str
