from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import PermitApplication, db
from app.schemas.permit_schema import permits_schema

bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@bp.route('/approve/<int:permit_id>', methods=['PUT'])
@jwt_required()
def approve_permit(permit_id):
    try:
        user = get_jwt_identity()
        if user['role'] != 'admin':
            return jsonify({'msg': 'Admins only'}), 403

        permit = PermitApplication.query.get(permit_id)
        if not permit:
            return jsonify({'msg': 'Permit not found'}), 404

        if permit.status != 'pending':
            return jsonify({'msg': 'Permit is not in pending status'}), 400

        permit.status = 'approved'
        db.session.commit()
        return jsonify({'msg': 'Permit approved'})

    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Internal server error"}), 500

@bp.route('/reject/<int:permit_id>', methods=['PUT'])
@jwt_required()
def reject_permit(permit_id):
    try:
        user = get_jwt_identity()
        if user['role'] != 'admin':
            return jsonify({'msg': 'Admins only'}), 403

        permit = PermitApplication.query.get(permit_id)
        if not permit:
            return jsonify({'msg': 'Permit not found'}), 404

        if permit.status != 'pending':
            return jsonify({'msg': 'Permit is not in pending status'}), 400

        permit.status = 'rejected'
        db.session.commit()
        return jsonify({'msg': 'Permit rejected'})

    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Internal server error"}), 500

@bp.route('/permits', methods=['GET'])
@jwt_required()
def list_all_permits():
    try:
        user = get_jwt_identity()
        if user['role'] != 'admin':
            return jsonify({'msg': 'Admins only'}), 403

        permits = PermitApplication.query.all()
        result = permits_schema.dump(permits)
        return jsonify(result)

    except Exception as e:
        return jsonify({"msg": "Internal server error"}), 500
