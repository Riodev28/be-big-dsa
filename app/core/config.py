from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cache_url: str
    ai_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
