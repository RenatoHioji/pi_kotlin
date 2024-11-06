import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash
from .db import db, user_history
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'app_user'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    my_items = db.relationship("Item", backref="author", lazy=True)
    item_history = db.relationship("Item", secondary=user_history, lazy='subquery', backref=db.backref("users", lazy=True))
    
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
    
    def get_history(self):
        history = []
        for item in self.item_history:
            history.append(item.serialize())
        return history
    
    def get_profile(self):
        return {
            "username": self.username,
            "email": self.email,
            "my_items": self.my_items
        }
    def get_items(self):
        list_items= []
        for item in self.my_items:
            list_items.append(item.serialize())
        return list_items
    
    @staticmethod
    def seed_user():
        if not User.query.first():
            user = User(username="teste", email="admin@example.com", password=generate_password_hash("admin", method="scrypt"))
            db.session.add(user)
            db.session.commit()
        else:
            pass