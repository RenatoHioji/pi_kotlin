from .db import db, game_list
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
    def seed_game(Quiz):
    def seed_game(Quiz):
        if not Game.query.first():
            games = [
                Game(correct_answer=0, type=0),
                Game(correct_answer=2, type=0),
                Game(correct_answer=1, type=0),
                Game(correct_answer=1, type=2),
                Game(correct_answer=3, type=0),
                Game(correct_answer=2, type=1),
            ]            
            db.session.add_all(games)
            db.session.add_all(games)
            db.session.commit()
            
            games = Game.query.all()
            quizzes = Quiz.query.all()
            values = [
                {'game_id': games[0].id, 'quiz_id': quizzes[0].id},
                {'game_id': games[1].id, 'quiz_id': quizzes[0].id},
                {'game_id': games[2].id, 'quiz_id': quizzes[1].id},
                {'game_id': games[3].id, 'quiz_id': quizzes[1].id},
                {'game_id': games[4].id, 'quiz_id': quizzes[2].id},
                {'game_id': games[5].id, 'quiz_id': quizzes[2].id},
            ]
            db.session.execute(game_list.insert(), values)
            db.session.commit()
        else:
            pass
            