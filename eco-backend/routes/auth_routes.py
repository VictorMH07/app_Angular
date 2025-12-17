from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.models import Usuario
from db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    if not nombre or not correo or not contrasena:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    if Usuario.query.filter_by(correo=correo).first():
        return jsonify({'error': 'Correo ya existe'}), 400
    
    usuario = Usuario(nombre=nombre, correo=correo)
    usuario.set_password(contrasena)
    db.session.add(usuario)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado exitosamente', 'usuario': usuario.to_dict()}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    usuario = Usuario.query.filter_by(correo=correo).first()
    if not usuario or not usuario.check_password(contrasena):
        return jsonify({'error': 'Credenciales inválidas'}), 401
    
    access_token = create_access_token(identity=str(usuario.id))
    return jsonify({'message': 'Login exitoso', 'access_token': access_token, 'usuario': usuario.to_dict()}), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    usuario = Usuario.query.get(int(current_user_id))
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(usuario.to_dict()), 200
