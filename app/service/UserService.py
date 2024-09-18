from models.User import User
from repository.UserRepository import UserRepository
from sqlalchemy.exc import IntegrityError
from utils.hash.password import verify_password
from flask import session
class UserService():
    def register(user: User):
        try:
            UserRepository.register(user)
            return {"message": "Usuário cadastrado com sucesso"}
        except IntegrityError as e:
            return {"error": "Usuário com esse email ou senha já existe"}
        
        except Exception as e:
            return {"error": f"{e}"}
    
    def login(user: User):
        try:
            userRegistered = UserRepository.findByEmail(user.email)
            if userRegistered and verify_password(userRegistered.password, user.password):
                session['user_id'] = user.id
                session['email'] = user.username
                return {"message": "Usuário logado com sucesso"}
            else:
                return {"error": "Usuário email e/ou senhas incorretas ou usuário inexistente"}
            
            
                
                
                     
        
            