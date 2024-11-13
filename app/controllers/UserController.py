from flask import request, jsonify, abort, session
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.UserService import UserService
from uuid import UUID
import uuid
from utils.id_converter import id_converter
import logging

logging.basicConfig(level=logging.DEBUG)

class UserController():
    def init_app(app):
        @app.route("/hello-world", methods=["GET"])
        def helloWorld():
            logging.info("Controller - Hello World")
            return jsonify({"success": True, "message": "Hello World"}), 200
        
        @app.route("/register", methods=["POST"])
        def register():
            logging.info("Controller - Registro")
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
            
        @app.route("/logar", methods=["POST"])
        def login():
            logging.info("Controller - Login")
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")
            user = User(email = email, password= password)
            result = UserService.login(user)
            return jsonify({"message": "Usuário logado com sucesso!", "user_id": result.id}), 200   
        
        @app.route("/user/<string:id>", methods=["GET"])
        def find_user_by_id(id: str):
            logging.info("Controller - Find By Id")
            user_id = id_converter.convert_id_uuid(id)
            user = UserService.find_user_by_id(user_id)
            return jsonify({"message": "Usuário encontrado com sucesso", "user": user}), 200           

        @app.route("/user/<string:id>", methods=["PUT"])
        def update_user(id: str):
            logging.info("Controller - Update User")
            
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            user_id = id_converter.convert_id_uuid(id)
           
            if not username or not email or not password:
                abort(400, description="Usuário, email ou senha estão faltando")
            hashed_password = hash_password(password)
            user = User(username, email, hashed_password)
            UserService.update_user(user, user_id)
            return jsonify({"message": "Usuário atualizado com sucesso"}), 200
            
        @app.route("/user/<string:id>", methods=["DELETE"])
        def delete_user(id: str):
            logging.info("Controller - Delete User")
            user_id = id_converter.convert_id_uuid(id)
            UserService.delete(user_id)
            return jsonify({"message": "Usuário deletado com sucesso"}), 204
        
        @app.route("/user/<string:id>/recents", methods=["GET"])
        def find_user_history(id: str):
            logging.info("Controller - Find By User History")
            
            user_id = id_converter.convert_id_uuid(id)
            history = UserService.find_user_history(user_id)
            return jsonify({"message": "Histórico de itens encontrados com sucesso", "history": history}), 200
    
        @app.route("/user/<string:id>/items", methods = ["GET"])
        def my_items(id: str ):
            logging.info("Controller - Find user itens")
            
            user_id = id_converter.convert_id_uuid(id)
            userItems = UserService.find_user_items(user_id)
            return jsonify({"message": "Itens encontrados com sucesso", "items": userItems})
        
        @app.route("/user/<string:id>/more_viewed", methods = ["GET"])
        def find_more_view_by_user(id: str):
            logging.info("Controller - Find more viewed itens")
            
            user_id = id_converter.convert_id_uuid(id)
            more_view_items = UserService.find_more_view_items(user_id)
            return jsonify({"message": "Items mais vistos encontrados", "items": more_view_items})