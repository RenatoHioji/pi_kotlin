from flask import request, jsonify, abort
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.UserService import UserService
from sqlalchemy.exc import IntegrityError
class UserController():
    @app.before_request
        def check_auth():
            routes = ['login', 'register', '/hello-world']
            if "user_id" not in session and request.endpoint not in routes:
                return {"error": "Usuário não está logado"}, 500
            
    def init_app(app):
        @app.route("/hello-world", methods=["GET"])
        def helloWorld():
            return jsonify({"success": True, "message": "Hello World"}), 200
        
        @app.route("/register", methods=["POST"])
        def register():
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            if not username or not email or not password:
                return jsonify({"error": "Alguns campos estão faltando"}), 400
                
            hashed_password = hash_password(password)
                
            user = User(username, email, hashed_password)
                
            result = UserService.register(user)
                
            if 'error' in result:
                return jsonify(result), 500
            return jsonify({"message": f"Usuário cadastrados com sucesso"}), 201
            
        @app.route("/login", methods=["POST"])
        def login():
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")
            
            if 'error' in result:
                return jsonify(result), 500
            return jsonify({"message": f"Usuário cadastrados com sucesso"}), 201