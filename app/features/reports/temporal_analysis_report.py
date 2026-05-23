from pydantic import BaseModel, ConfigDict

class TemporalAnalysisReport(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    time_complexity: str
    max_loop_depth: int
    recursive: bool