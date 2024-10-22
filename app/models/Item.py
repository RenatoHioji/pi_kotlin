import uuid
from sqlalchemy.dialects.postgresql import UUID
from .db import db
from typing import Optional
class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    syllables = db.Column(db.String(255), nullable = False)
    img = db.Column(db.String(255), unique=False, nullable=False)
    video = db.Column(db.String(255), unique = False, nullable = False)
    category = db.Column(db.String(255), unique = False, nullable = True)
    subcategory = db.Column(db.String(255), unique = False, nullable= True)   
    
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=True)
    
    
    def __init__(self, name: str, syllables: str, img: str, video: str, category: Optional[str] = None, subcategory: Optional[str] = None):
        self.name = name
        self.syllables = syllables
        self.img = img
        self.video = video
        self.category = category
        self.subcategory = subcategory
    
    def serialize(item):
        return {
            "id": item.id,
            "name": item.name,
            "syllables": item.syllables,
            "img": item.img,
            "video": item.video,
            "category": item.category,
            "subcategory": item.subcategory
        }
    @staticmethod
    def seed_item():
        if not Item.query.first():
            pass