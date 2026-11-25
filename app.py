"""Render's configured gunicorn app:app entry point."""
from backend.app import app

from agent_bridge import register_agent_bridge
register_agent_bridge(app, agent_id="ionos_ai", display_name="IONOS AI", persona="Du verbindest bestehende KI-Module, analysierst Backend-Architektur und bewahrst vorhandene Projektfunktionen.")

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '10000')))
