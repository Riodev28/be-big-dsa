from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TemporalAnalysisReport:
    time_complexity: str
    max_loop_depth: int
    recursive: bool
