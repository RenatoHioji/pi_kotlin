from models.Quiz import Quiz
class QuizRepository:
    def find_all():
        return Quiz.query.all()
    
    def find_by_id(id):
        return Quiz.query.filter_by(id=id).first()
    
    def find_by_nivel(nivel):
        return Quiz.query.filter_by(nivel=nivel).all()