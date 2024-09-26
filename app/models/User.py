import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash
from .db import db
from sqlalchemy.orm import relationship
class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    items = relationship("Item", back_populates="user", cascade="all, delete-orphan")
         
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
    
    @staticmethod
    def seed_user():
        if not User.query.first():
            user = User(username="admin", email="admin@example.com", password=generate_password_hash("admin", method="scrypt"))
            db.session.add(user)
            db.session.commit()
            print("Usuário adicionado com sucesso")
        else:
            print("Usuários já existentes")
