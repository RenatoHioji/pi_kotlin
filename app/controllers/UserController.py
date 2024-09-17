from flask import request, jsonify, abort
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.UserService import UserService

class UserController():
    def init_app(app):
        @app.route("/hello-world", methods="GET")
        def helloWorld():
            return jsonify({"success", "Hello World"}), 200
        
        @app.route("/register", methods="POST")
        def register():
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            if not username or not email or not password:
                return jsonify({"error": "Missing required fields"}), 400
            hashed_password = hash_password(password)
            try:
                user = User(username, email, hashed_password)
                registeredUser = UserService.register(user)
                if(registeredUser):
                    return jsonify({"message": "User registered successfully"}), 201
            except OperationalError as e:
                return jsonify({"error": "Couldn't create user with this info"}), 400
            @app.route("/login", methods="POST")
            def login():
                data = request.get_json()
                email = data.get("email")
                password = data.get("password")
    
                if not email or not password:
                    return jsonify({"error": "Missing email or password"})
                try:
                    UserService.login(email, password)
                except OperationalError as e:
                    return jsonify({"error": f"Failed to login with error {e}"})

