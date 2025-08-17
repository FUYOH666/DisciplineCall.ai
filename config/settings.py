"""
Configuration settings for DisciplineCall.ai
Supports both cloud and local deployment modes
"""

from pydantic_settings import BaseSettings
from typing import Optional, List
from enum import Enum


class DeploymentMode(str, Enum):
    """Deployment mode options"""
    CLOUD = "cloud"
    LOCAL = "local"
    HYBRID = "hybrid"


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Application settings
    app_name: str = "DisciplineCall.ai"
    app_version: str = "0.1.0"
    debug: bool = False
    deployment_mode: DeploymentMode = DeploymentMode.CLOUD
    
    # API settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 1
    
    # Database settings
    database_url: str = "postgresql://user:password@localhost/disciplinecall"
    redis_url: str = "redis://localhost:6379/0"
    
    # AI providers (Cloud mode)
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    elevenlabs_api_key: Optional[str] = None
    
    # Local AI models (Local mode)
    local_llm_model: str = "llama2"
    local_tts_model: str = "coqui"
    local_stt_model: str = "whisper"
    
    # Communication providers
    twilio_account_sid: Optional[str] = None
    twilio_auth_token: Optional[str] = None
    twilio_phone_number: Optional[str] = None
    
    telegram_bot_token: Optional[str] = None
    whatsapp_api_token: Optional[str] = None
    whatsapp_phone_number_id: Optional[str] = None
    
    # Google Sheets integration
    google_credentials_path: Optional[str] = None
    google_sheets_enabled: bool = False
    
    # Payment processing
    stripe_api_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None
    penalty_enabled: bool = False
    
    # Security settings
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/disciplinecall.log"
    
    # Call scheduling
    default_morning_time: str = "08:00"
    default_midday_time: str = "13:00"
    default_evening_time: str = "20:00"
    max_call_duration: int = 300  # seconds
    
    # Voice settings
    default_voice_provider: str = "elevenlabs"
    voice_speed: float = 1.0
    voice_stability: float = 0.5
    
    # Features flags
    penalty_system_enabled: bool = True
    multi_language_enabled: bool = False
    analytics_enabled: bool = True
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class CloudSettings(Settings):
    """Settings for cloud deployment"""
    
    deployment_mode: DeploymentMode = DeploymentMode.CLOUD
    
    # Required cloud services
    openai_api_key: str
    elevenlabs_api_key: str
    twilio_account_sid: str
    twilio_auth_token: str
    
    # Optional cloud enhancements
    sentry_dsn: Optional[str] = None
    analytics_provider: str = "mixpanel"


class LocalSettings(Settings):
    """Settings for local/private deployment"""
    
    deployment_mode: DeploymentMode = DeploymentMode.LOCAL
    
    # Local model paths
    local_models_path: str = "./models"
    local_data_path: str = "./user_data"
    
    # Privacy settings
    data_retention_days: int = 90
    encryption_enabled: bool = True
    local_only: bool = True
    
    # Local service ports
    redis_port: int = 6379
    postgres_port: int = 5432


# Configuration factory
def get_settings(mode: Optional[DeploymentMode] = None) -> Settings:
    """Get appropriate settings based on deployment mode"""
    
    if mode == DeploymentMode.CLOUD:
        return CloudSettings()
    elif mode == DeploymentMode.LOCAL:
        return LocalSettings()
    else:
        # Auto-detect based on environment
        import os
        if os.getenv("DEPLOYMENT_MODE") == "local":
            return LocalSettings()
        else:
            return CloudSettings()


# Default settings instance
settings = get_settings()


# Voice personality configurations
PERSONALITY_CONFIGS = {
    "motivator": {
        "voice_style": "energetic",
        "speaking_rate": 1.1,
        "enthusiasm_level": "high",
        "keywords": ["amazing", "fantastic", "you've got this"]
    },
    "drill_sergeant": {
        "voice_style": "stern",
        "speaking_rate": 1.0,
        "volume_level": "loud",
        "keywords": ["discipline", "no excuses", "push harder"]
    },
    "abuser": {
        "voice_style": "sarcastic",
        "speaking_rate": 0.9,
        "humor_level": "high",
        "keywords": ["really?", "seriously?", "come on"]
    },
    "friend": {
        "voice_style": "friendly",
        "speaking_rate": 0.95,
        "warmth_level": "high",
        "keywords": ["understand", "together", "support"]
    },
    "mentor": {
        "voice_style": "wise",
        "speaking_rate": 0.85,
        "patience_level": "high",
        "keywords": ["consider", "reflect", "growth"]
    }
}


# Call timing configurations
CALL_TEMPLATES = {
    "morning": {
        "duration": 120,  # seconds
        "topics": ["goals", "energy", "priorities", "mood"],
        "tone": "energetic"
    },
    "midday": {
        "duration": 90,
        "topics": ["progress", "focus", "nutrition", "challenges"],
        "tone": "supportive"
    },
    "evening": {
        "duration": 150,
        "topics": ["reflection", "wins", "lessons", "tomorrow"],
        "tone": "calming"
    }
}
