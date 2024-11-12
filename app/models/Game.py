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
    
    def serialize(game):
        return {
            "id": game.id,
            "correct_answer": game.correct_answer,
            "type": game.type,
            "game_items": game.game_items,
            "quiz_id": game.quiz_id
        }
    def serialize_list(games):
        game_list = []
        for game in games:
            game_list.append(game.serialize())
        return game_list
    @staticmethod
    def seed_game(quiz, quiz2, quiz3):
        # Pato uva sim madeira
        if not Game.query.first():
            games = [
                Game(correct_answer=0, type=0, quiz_id=quiz.id),
                Game(correct_answer=1, type=0, quiz_id=quiz.id),
                Game(correct_answer=2, type=0, quiz_id=quiz.id),
                Game(correct_answer=1, type=2, quiz_id=quiz.id),
                Game(correct_answer=3, type=0, quiz_id=quiz.id),
                Game(correct_answer=2, type=1, quiz_id=quiz2.id),
                Game(correct_answer=1, type=2, quiz_id=quiz2.id),
                Game(correct_answer=0, type=1, quiz_id=quiz2.id),
                Game(correct_answer=2, type=0, quiz_id=quiz2.id),
                Game(correct_answer=2, type=1, quiz_id=quiz2.id),
                Game(correct_answer=1, type=0, quiz_id=quiz3.id),
                Game(correct_answer=0, type=2, quiz_id=quiz3.id),
                Game(correct_answer=2, type=1, quiz_id=quiz3.id),
                Game(correct_answer=2, type=1, quiz_id=quiz3.id),
                Game(correct_answer=0, type=0, quiz_id=quiz3.id)
            ]            
            for game in games:
                db.session.add(game)
            db.session.commit()
        else:
            pass
            