"""
WSGI Entry Point
Für Gunicorn / Production Deployment
"""

import os
from app import create_app

# Create Flask app
config_name = os.getenv("FLASK_ENV", "development")
app = create_app(config_name)

if __name__ == "__main__":
    # Development server
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.getenv("FLASK_DEBUG", "False") == "True"
    )

