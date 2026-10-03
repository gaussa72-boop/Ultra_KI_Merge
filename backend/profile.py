from ..database import db
from datetime import datetime
import json

class Profile(db.Model):
    """User Profile & Personality Model"""
    __tablename__ = "profiles"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Personality attributes
    tone = db.Column(db.String(50), default="neutral")  # mystisch, strategisch, kreativ, etc.
    depth = db.Column(db.String(50), default="standard")  # einfach, standard, erweitert
    style = db.Column(db.String(50), default="digital")  # spirituell, wissenschaftlich, kreativ
    mode = db.Column(db.String(50), default="assistant")  # assistant, creator, game_master
    
    # Evolution tracking
    level = db.Column(db.Integer, default=1)  # 1-10 Evolutionsstufen
    interaction_count = db.Column(db.Integer, default=0)
    preferred_genre = db.Column(db.String(100))
    
    # Custom settings
    settings = db.Column(db.Text, default="{}")  # JSON
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def get_settings(self):
        return json.loads(self.settings) if self.settings else {}
    
    def set_settings(self, settings_dict):
        self.settings = json.dumps(settings_dict)
    
    def to_dict(self):
        return {
            "tone": self.tone,
            "depth": self.depth,
            "style": self.style,
            "mode": self.mode,
            "level": self.level,
            "interaction_count": self.interaction_count,
            "preferred_genre": self.preferred_genre,
            "settings": self.get_settings()
        }

