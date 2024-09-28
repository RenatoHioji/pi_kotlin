from flask import jsonify

class ControllerAdvice():
    def init_app(app):
        @app.errorhandler(404)
        def not_found(e):
            description = e.description if e.description else "Error 404"
            return jsonify({"error": description}), 404
        @app.errorhandler(400)
        def not_found(e):
            description = e.description if e.description else "Error 400"
            return jsonify({"error": description}), 400
        @app.errorhandler(500)
        def not_found(e):
            description = e.description if e.description else "Error 500"
            return jsonify({"error": description}), 500