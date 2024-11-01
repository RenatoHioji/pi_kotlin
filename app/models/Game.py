from .db import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    correct_answer = db.Column(db.Integer, unique=False, nullable=False)
    type =  db.Column(db.Integer, unique=False, nullable=False)
    
    game_items = db.relationship("Item", backref="item_owner", lazy=True)
    quiz_id = db.Column(UUID(as_uuid=True), db.ForeignKey('quiz.id'), nullable=True)
    
    @staticmethod
    def seed_game():
        if not Game.query.first():
            game = Game(correct_answer=0, type=0)
            db.session.add(game)
            db.session.commit()
        else:
            pass
            