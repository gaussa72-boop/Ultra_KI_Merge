"""
Quantum Meta Core Application Factory
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

from .database import db, init_db
from .config import config

def create_app(config_name=None):
    """Application factory"""
    
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "development")
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    JWTManager(app)
    CORS(app)
    
    # Initialize database
    with app.app_context():
        init_db(app)
    
    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.ai import ai_bp
    from .routes.companion import companion_bp
    from .routes.game import game_bp
    from .routes.profile import profile_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(companion_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(profile_bp)
    
    # Health check endpoint
    @app.route("/health", methods=["GET"])
    def health():
        return {
            "status": "healthy",
            "service": "Quantum Meta Core",
            "version": "1.0.0"
        }, 200
    
    # Root endpoint
    @app.route("/", methods=["GET"])
    def index():
        return {
            "message": "Welcome to Quantum Meta Core",
            "version": "1.0.0",
            "endpoints": {
                "auth": "/api/auth",
                "ai": "/api/ai",
                "companion": "/api/companion",
                "game": "/api/game",
                "profile": "/api/profile"
            }
        }, 200
    
    return app

