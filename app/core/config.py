from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cors_origins: list[str] = [
        "http://localhost:3001"
    ]
    
    cache_url: str
    ai_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
