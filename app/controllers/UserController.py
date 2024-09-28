from flask import request, jsonify, abort, session
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.UserService import UserService
from sqlalchemy.exc import IntegrityError
from uuid import UUID
import uuid


class UserController():
    def init_app(app):
        @app.before_request
        def check_auth():
            routes = ['login', 'register', '/hello-world']
            if "user_id" not in session and request.endpoint not in routes:
                abort(500, description="Usuário não está logado")

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
                abort(400, description="Usuário, email ou senha estão faltando")
            hashed_password = hash_password(password)
            user = User(username, email, hashed_password)
            result = UserService.register(user)
            return jsonify({"message": f"Usuário cadastrado com sucesso"}), 201
            
        @app.route("/login", methods=["POST"])
        def login():
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")
            user = User(email = email, password= password)
            result = UserService.login(user)
            return jsonify({"message": "Usuário logado com sucesso!"}), 200   
        
        @app.route(f"/user/recents/<string:user_id>", methods=["GET"])
        def findUserHistory(user_id: str):
            if not user_id:
                abort(400, "Id de usuário não foi enviado")
            try:
                id = uuid.UUID(user_id)
            except Exception as e:
                abort(400, "Id de usuário não pode ser transformado em UUID")
            history = UserService.findUserHistory(id)
            return jsonify({"message": "Histórico de itens encontrados com sucesso", "history": history}), 200
        