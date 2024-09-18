import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash
from .db import db

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    def __init__(self, username, email, password=None):
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password, method="scrypt")
    
    @staticmethod
    def seed_user():
        if not User.query.first():
            user = User(username="admin", email="admin@example.com", password="admin")
            db.session.add(user)
            db.session.commit()
            print("Usuário adicionado com sucesso")
        else:
            print("Usuários já existentes")
