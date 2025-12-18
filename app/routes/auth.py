from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app import db
from app.models import User
from app.schemas.user_schema import user_schema
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "No input data provided"}), 400

        # Validate input data
        validated_data = user_schema.load(data)

        # Check if user already exists
        existing_user = User.query.filter_by(username=validated_data['username']).first()
        if existing_user:
            return jsonify({"msg": "Username already exists"}), 409

        # Create new user
        new_user = User(**validated_data)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "Registered successfully"}), 201

    except ValidationError as err:
        return jsonify({"msg": "Validation error", "errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Internal server error"}), 500

@bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"msg": "No input data provided"}), 400

        # Basic validation
        if not data.get('username') or not data.get('password'):
            return jsonify({"msg": "Username and password are required"}), 400

        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            token = create_access_token(identity={'id': user.id, 'role': user.role})
            return jsonify(access_token=token)
        return jsonify({"msg": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"msg": "Internal server error"}), 500
