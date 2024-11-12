import uuid
from sqlalchemy.dialects.postgresql import UUID
from .db import db
from .Game import Game

class Quiz(db.Model):
    __tablename__ = "quiz"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nivel = db.Column(db.Integer, unique=False, nullable=False)
    quiz_game_list = db.relationship("Game", backref="game_owner", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "nivel": self.nivel,
            "quiz_game_list": self.quiz_game_list
        }
    
    def serialize_list(quizzes):
        quiz_list = []
        for quiz in quizzes:
            quiz_list.append(quiz.serialize())
        return quiz_list
    @staticmethod
    def seed_quiz():
        if not Quiz.query.first():
            quizzes = [
                Quiz(nivel = 0),
                Quiz(nivel = 1),
                Quiz(nivel = 2)
            ]           
                
            db.session.add(quiz)
            db.session.commit()
            
        else:
            pass