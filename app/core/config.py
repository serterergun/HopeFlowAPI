import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FastAPI App")
    API_VERSION: str = os.getenv("API_VERSION", "v1")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Database Config
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    # CORS
    # BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS").split(",")

settings = Settings()