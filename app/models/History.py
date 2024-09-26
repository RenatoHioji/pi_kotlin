import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import db

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    item_id = db.Column(Integer, ForeignKey('item.id'))
    timestamp = db.Column(DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='histories')
    item = relationship('Item', back_populates='users')
    
    def __init__(self, user_id, item_id):
        self.user_id = user_id
        self.item_id = item_id
