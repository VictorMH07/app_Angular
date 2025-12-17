from app import app
from db import db
from models.models import Usuario

with app.app_context():
    admin = Usuario(
        nombre='Administrador',
        correo='admin@ecomarket.com',
        rol='admin'
    )
    admin.set_password('admin123')

    db.session.add(admin)
    db.session.commit()

    print('Administrador creado correctamente')