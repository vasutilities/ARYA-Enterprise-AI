"""Centralized application environment configuration."""

import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=os.environ.get("ENV_FILE", ".env"), extra="ignore")
    AWS_ACCESS_KEY_ID: str 
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str = "us-east-2"
    BEDROCK_EMBED_MODEL: str
    BEDROCK_CHAT_MODEL: str
    S3_BUCKET_NAME: str
    BEDROCK_EMBED_MODEL: str = "amazon.titan-embed-text-v2:0"
    BEDROCK_CHAT_MODEL: str = "amazon.nova-lite-v1:0"
    EMBED_DIMENSION: int = 1024
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str
    PINECONE_CLOUD: str = "aws"
    PINECONE_ENVIRONMENT: str
    PINECONE_READ_TIMEOUT: int = 180
    database_url: str
    conversation_memory: int = 6
    max_upload_bytes: int = 10485760

@lru_cache()
def get_settings() -> Settings:
    """Get application settings with caching."""
    return Settings()