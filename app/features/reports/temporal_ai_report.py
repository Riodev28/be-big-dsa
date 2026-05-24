from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TemporalAIReport:
    temporal_explanation: str
