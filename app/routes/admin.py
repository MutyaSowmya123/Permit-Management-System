from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import PermitApplication, db

bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@bp.route('/approve/<int:permit_id>', methods=['PUT'])
@jwt_required()
def approve_permit(permit_id):
    user = get_jwt_identity()
    if user['role'] != 'admin':
        return jsonify({'msg': 'Admins only'}), 403

    permit = PermitApplication.query.get(permit_id)
    if not permit:
        return jsonify({'msg': 'Permit not found'}), 404

    permit.status = 'approved'
    db.session.commit()
    return jsonify({'msg': 'Permit approved'})
