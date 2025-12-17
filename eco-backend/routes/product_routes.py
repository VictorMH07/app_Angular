from flask import Blueprint, jsonify, request
from db import db
from models.models import Producto
from sqlalchemy.exc import IntegrityError

product_bp = Blueprint('product_bp', __name__)

# Obtener todos los productos
@product_bp.route('/', methods=['GET'])
def get_all_products():
    try:
        productos = Producto.query.all()
        return jsonify([p.to_dict() for p in productos]), 200
    except Exception as e:
        return jsonify({"error": "Error al obtener los productos", "detail": str(e)}), 500

#  Obtener un producto por ID
@product_bp.route('<int:id>', methods=['GET'])
def get_product(id):
    try:
        producto = Producto.query.get(id)
        if producto:
            return jsonify(producto.to_dict()), 200
        return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": "Error al obtener el producto", "detail": str(e)}), 500

# Crear producto
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido o body vacío"}), 400

    # Aceptar claves tanto en español como en inglés (fallbacks)
    nombre = data.get('nombre') or data.get('name')
    descripcion = data.get('descripcion') or data.get('description') or ''
    precio = data.get('precio') or data.get('price')
    imagen = data.get('imagen') or data.get('image') or ''

    # Validaciones básicas
    if not nombre:
        return jsonify({"error": "El campo 'nombre' es requerido"}), 400
    if precio is None:
        return jsonify({"error": "El campo 'precio' es requerido"}), 400

    try:
        precio = float(precio)
    except (TypeError, ValueError):
        return jsonify({"error": "El campo 'precio' debe ser numérico"}), 400

    nuevo = Producto(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio,
        imagen=imagen
    )

    try:
        db.session.add(nuevo)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Error de integridad en la base de datos", "detail": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear producto", "detail": str(e)}), 500

    return jsonify(nuevo.to_dict()), 201

# Actualizar producto
@product_bp.route('<int:id>', methods=['PUT'])
def update_producto(id):
    try:
        producto = Producto.query.get(id)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "JSON inválido o body vacío"}), 400

        # Actualización de campos (solo los que vienen)
        producto.nombre = data.get('nombre', producto.nombre)
        producto.descripcion = data.get('descripcion', producto.descripcion)
        producto.precio = data.get('precio', producto.precio)
        producto.imagen = data.get('imagen', producto.imagen)

        db.session.commit()
        return jsonify(producto.to_dict()), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Error de integridad al actualizar", "detail": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el producto", "detail": str(e)}), 500

# Eliminar producto
@product_bp.route('<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        producto = Producto.query.get(id)
        if not producto:
            return jsonify({"error": "Producto no encontrado"}), 404

        db.session.delete(producto)
        db.session.commit()
        return jsonify({"message": f"Producto '{producto.nombre}' eliminado correctamente"}), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Error de integridad al eliminar", "detail": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar producto", "detail": str(e)}), 500