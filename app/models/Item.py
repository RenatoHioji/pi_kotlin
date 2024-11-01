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
    
    game_id = db.Column(UUID(as_uuid=True), db.ForeignKey('game.id'), nullable=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=True)
    
    def __init__(self, name: str, syllables: str, img: str, video: str, category: Optional[str] = None, subcategory: Optional[str] = None, user_id: Optional[str] = None, game_id: Optional[str] = None ):
        self.name = name
        self.syllables = syllables
        self.img = img
        self.video = video
        self.category = category
        self.subcategory = subcategory
        self.user_id = user_id
        self.game_id = game_id
    
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
    def serialize_list(items):
        item_list = []
        for item in items:
            item_list.append(item.serialize())
        return item_list

    @staticmethod
    def seed_item():
        if not Item.query.first():
            item = Item(name="teste", syllables="tes - te", img="teste.webp", video="teste", category="teste", subcategory="teste")
            item2 = Item(name="teste", syllables="tes - te", img="teste.webp", video="teste", subcategory="teste")
            item3 = Item(name="teste", syllables="tes - te", img="teste.webp", video="teste", category="teste")
            db.session.add(item)
            db.session.add(item2)
            db.session.add(item3)
            db.session.commit()
        else:
            pass
            