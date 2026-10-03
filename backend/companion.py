"""
Companion Routes
KI-Begleiter Kommunikation
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..core.companion_core import create_companion
from ..models.user import User
from ..database import db

companion_bp = Blueprint("companion", __name__, url_prefix="/api/companion")

@companion_bp.route("/speak", methods=["POST"])
@jwt_required()
def companion_speak():
    """Companion responds to user"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        data = request.get_json()
        message = data.get("message", "")
        
        # Get companion with user profile
        profile = user.profile.to_dict() if user.profile else {}
        companion = create_companion(profile)
        
        # Generate response
        response = companion.respond(message)
        
        return jsonify({
            "success": True,
            "companion_response": response,
            "tone": profile.get("tone", "neutral"),
            "level": user.profile.level if user.profile else 1
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@companion_bp.route("/status", methods=["GET"])
@jwt_required()
def companion_status():
    """Get companion status"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or not user.profile:
            return jsonify({"error": "No profile found"}), 404
        
        profile = user.profile.to_dict()
        
        return jsonify({
            "status": "active",
            "name": f"Companion_{user.username}",
            "tone": profile.get("tone"),
            "level": profile.get("level"),
            "mood": profile.get("mood", "neutral"),
            "interaction_count": profile.get("interaction_count", 0)
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@companion_bp.route("/personality", methods=["PUT"])
@jwt_required()
def update_personality():
    """Update companion personality"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user or not user.profile:
            return jsonify({"error": "No profile found"}), 404
        
        data = request.get_json()
        
        # Update personality traits
        if "tone" in data:
            user.profile.tone = data["tone"]
        if "mood" in data:
            user.profile.settings = str({**user.profile.get_settings(), "mood": data["mood"]})
        if "style" in data:
            user.profile.style = data["style"]
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "profile": user.profile.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

