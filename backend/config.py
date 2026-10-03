import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base Configuration"""
    SECRET_KEY = os.getenv("SECRET_KEY", "QUANTUM_ULTRA_SECRET_2026")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "JWT_QUANTUM_SECRET_2026")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///quantum_dev.db"
    )
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

class ProductionConfig(Config):
    """Production Configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://quantum_user:securepassword@postgres:5432/quantum_db"
    )
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

class TestingConfig(Config):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    REDIS_URL = "redis://localhost:6379/1"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

