from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import PermitApplication

bp = Blueprint('permit', __name__, url_prefix='/api/permit')

@bp.route('/submit', methods=['POST'])
@jwt_required()
def submit():
    user = get_jwt_identity()
    data = request.get_json()
    permit = PermitApplication(user_id=user['id'], description=data['description'])
    db.session.add(permit)
    db.session.commit()
    return jsonify({"msg": "Permit submitted"}), 201

@bp.route('/my-permits', methods=['GET'])
@jwt_required()
def list_user_permits():
    user = get_jwt_identity()
    permits = PermitApplication.query.filter_by(user_id=user['id']).all()
    return jsonify([{'id': p.id, 'desc': p.description, 'status': p.status} for p in permits])
