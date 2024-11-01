import uuid
from sqlalchemy.dialects.postgresql import UUID
from .db import db

class Quiz(db.Model):
    __tablename__ = "quiz"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nivel = db.Column(db.Integer, unique=False, nullable=False)
    quiz_game_list = db.relationship("Game", backref="game_owner", lazy=True)

    
    @staticmethod
    def seed_quiz():
        if not Quiz.query.first():
            quiz = Quiz(nivel = 0)
            db.session.add(quiz)
            db.session.commit()
        else:
            pass