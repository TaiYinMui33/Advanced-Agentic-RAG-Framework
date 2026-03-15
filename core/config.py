from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Enterprise RAG API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Vector DB config
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    
    # LLM config
    OPENAI_API_KEY: str = ""
    MODEL_NAME: str = "gpt-4-turbo"
    
    class Config:
        env_file = ".env"

settings = Settings()
