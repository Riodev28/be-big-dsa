from groq import Groq
from groq.types.chat import ChatCompletion
from ...core.config import settings


class AI:
    def __init__(self):
        self.ai = Groq(api_key=settings.ai_api_key)

    @staticmethod
    def create_client() -> "AI":
        return AI()

    async def create_response(self, model: str, prompt: str) -> ChatCompletion:
        return self.ai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )

    def first_content(self, response: ChatCompletion):
        return response.choices[0].message.content
