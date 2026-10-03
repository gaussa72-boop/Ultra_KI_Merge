from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = __import__("os").getenv(
        "FLASK_SECRET_KEY", "dev-only-change-me"
    )
    from .routes import main
    app.register_blueprint(main)
    return app
