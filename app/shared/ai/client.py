from .ai import AI


def create_ai_client() -> AI:
    return AI.create_client()
