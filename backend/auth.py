"""
Authentication Routes
Login, Register, JWT Management
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from ..database import db
from ..models.user import User
from ..models.profile import Profile

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    """Register new user"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data.get("username") or not data.get("password") or not data.get("email"):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Check if user exists
        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"error": "Username already exists"}), 400
        
        # Create user
        user = User(
            username=data["username"],
            email=data["email"]
        )
        user.set_password(data["password"])
        
        db.session.add(user)
        db.session.commit()
        
        # Create profile
        profile = Profile(user_id=user.id)
        db.session.add(profile)
        db.session.commit()
        
        return jsonify({
            "message": "User registered successfully",
            "user": user.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    """Login user"""
    try:
        data = request.get_json()
        
        # Find user
        user = User.query.filter_by(username=data.get("username")).first()
        
        if not user or not user.check_password(data.get("password", "")):
            return jsonify({"error": "Invalid credentials"}), 401
        
        # Create JWT token
        token = create_access_token(identity=user.id)
        
        return jsonify({
            "message": "Login successful",
            "access_token": token,
            "user": user.to_dict()
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    """Get user profile"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({
            "user": user.to_dict(),
            "profile": user.profile.to_dict() if user.profile else {}
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route("/verify", methods=["GET"])
@jwt_required()
def verify_token():
    """Verify JWT token"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        return jsonify({
            "valid": True,
            "user_id": user_id,
            "username": user.username if user else None
        }), 200
    
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)}), 401

