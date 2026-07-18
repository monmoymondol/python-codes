from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token, jwt_required

user_bp = Blueprint("users", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.json
    user = User(username=data["username"], password=data["password"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered!"})

@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.json
    user = User.query.filter_by(username=data["username"], password=data["password"]).first()
    if user:
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
