from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager 
from db import db 
from routes.product_routes import product_bp
from routes.auth_routes import auth_bp
import os

app = Flask(__name__)
CORS(app, resources = {r"/*": {"origins": "*"}})

# Configuración JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-jwt-secret')
jwt = JWTManager(app)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "instance", "eco_market.db")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{db_path}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenido a la API de EcoMarket",
        "endpoints": {
            "products": "/api/products",
            "auth": {
                "register": "/api/auth/register",
                "login": "/api/auth/login",
                "profile": "/api/auth/profile"
            }
        }
    })

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello with flask!"})

# Registra blueprints
app.register_blueprint(product_bp, url_prefix='/api/products')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

with app.app_context():
    db.create_all()
    print("Base de datos creada correctamente (eco_market.db)")

if __name__ == '__main__':
    app.run(debug=True)
