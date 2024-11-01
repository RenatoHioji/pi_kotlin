from repository.QuizRepository import QuizRepository
from uuid import UUID
from flask import abort
from models.Quiz import Quiz
class QuizService():
    def find_all():
        return Quiz.serialize_list(QuizRepository.find_all())
    
    def find_by_id(id: UUID):
        quiz = QuizRepository.find_by_id(id)
        if not quiz:
            abort(404, description = f"Quiz não encontrado com id: {id}")
        return quiz.serialize()
    
    def find_by_nivel(nivel):
        quizzes = QuizRepository.find_by_nivel(nivel)
        if not quizzes:
            abort(404, description = f"Quizes não encontrado com nivel: {nivel}")
        return Quiz.serialize_list(quizzes)
            