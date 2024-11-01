from utils.id_converter import id_converter
from flask import request, abort
from service.QuizService import QuizService
class QuizControlller():
    def init_app(app):
        @app.route("/quizzes", methods=["GET"])
        def find_all_quiz():
            return QuizService.find_all()
        
        @app.route("/quiz/<string:id>", methods=["GET"])
        def find_quiz_by_id(id: str):
            item_id = id_converter.convert_id_uuid(id)
            return QuizService.find_by_id(item_id)
        
        @app.route("/quiz")
        def find_quiz_by_nivel():
            nivel = request.args.get("nivel")
            if not nivel:
                abort(404, description="Nível não foi enviado como parâmetro")
            return QuizService.find_by_nivel(nivel)