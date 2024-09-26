import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash
from .db import db
from typing import Optional
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    syllables = db.Column(db.String(255), nullable = False)
    img = db.Column(db.String(255), unique=False, nullable=False)
    audio = db.Column(db.String(255), unique = False, nullable = False)
    category = db.Column(db.String(255), unique = True, nullable = True)
    subcategory = db.Column(db.String(255), unique = True, nullable= True)   
    user_id = db.Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="items")
    
    def __init__(self, name: str, syllables: str, img: str, audio: str, category: Optional[str] = None, subcategory: Optional[str] = None):
        self.name = name
        self.syllables = syllables
        self.img = img
        self.audio = audio
        self.category = category
        self.subcategory = subcategory
    
    @staticmethod
    def seed_item():
        if not Item.query.first():
            pass