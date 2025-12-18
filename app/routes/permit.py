from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import PermitApplication
from app.schemas.permit_schema import permit_schema, permits_schema
from marshmallow import ValidationError

bp = Blueprint('permit', __name__, url_prefix='/api/permit')

@bp.route('/submit', methods=['POST'])
@jwt_required()
def submit():
    try:
        user = get_jwt_identity()
        data = request.get_json()
        if not data:
            return jsonify({"msg": "No input data provided"}), 400

        # Validate input data
        validated_data = permit_schema.load(data, partial=True)
        validated_data['user_id'] = user['id']

        # Create permit application
        permit = PermitApplication(**validated_data)
        db.session.add(permit)
        db.session.commit()

        result = permit_schema.dump(permit)
        return jsonify({"msg": "Permit submitted", "permit": result}), 201

    except ValidationError as err:
        return jsonify({"msg": "Validation error", "errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Internal server error"}), 500

@bp.route('/my-permits', methods=['GET'])
@jwt_required()
def list_user_permits():
    try:
        user = get_jwt_identity()
        permits = PermitApplication.query.filter_by(user_id=user['id']).all()
        result = permits_schema.dump(permits)
        return jsonify(result)
    except Exception as e:
        return jsonify({"msg": "Internal server error"}), 500

@bp.route('/<int:permit_id>', methods=['PUT'])
@jwt_required()
def update_permit(permit_id):
    try:
        user = get_jwt_identity()
        permit = PermitApplication.query.filter_by(id=permit_id, user_id=user['id']).first()

        if not permit:
            return jsonify({"msg": "Permit not found"}), 404

        if permit.status != 'pending':
            return jsonify({"msg": "Cannot update non-pending permit"}), 400

        data = request.get_json()
        if not data:
            return jsonify({"msg": "No input data provided"}), 400

        # Validate input data
        validated_data = permit_schema.load(data, partial=True)

        # Update permit
        for key, value in validated_data.items():
            setattr(permit, key, value)

        db.session.commit()

        result = permit_schema.dump(permit)
        return jsonify({"msg": "Permit updated", "permit": result})

    except ValidationError as err:
        return jsonify({"msg": "Validation error", "errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Internal server error"}), 500

@bp.route('/<int:permit_id>', methods=['DELETE'])
@jwt_required()
def delete_permit(permit_id):
    try:
        user = get_jwt_identity()
        permit = PermitApplication.query.filter_by(id=permit_id, user_id=user['id']).first()

        if not permit:
            return jsonify({"msg": "Permit not found"}), 404

        if permit.status != 'pending':
            return jsonify({"msg": "Cannot delete non-pending permit"}), 400

        db.session.delete(permit)
        db.session.commit()

        return jsonify({"msg": "Permit deleted"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Internal server error"}), 500
