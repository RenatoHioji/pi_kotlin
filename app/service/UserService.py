from models.User import User
from repository.UserRepository import UserRepository
from utils.hash.password import verify_password
from flask import session, abort
from uuid import UUID
class UserService():
    def register(user: User):
        UserRepository.register(user)
    def login(user: User):
        userRegistered = UserRepository.findByEmail(user.email)
        if userRegistered and verify_password(userRegistered.password, user.password):
            session['user_id'] = user.id
            session['email'] = user.username
            return 
        else:
            abort(404, description = "Usuário email e/ou senhas incorretas ou usuário inexistente")
                
    def findUserHistory(user_id: UUID):
        history = UserRepository.findUserHistory(user_id).get_history()
        if not history:
                abort(404, description = "Histórico não foi encontrado")
        return history
                
                     
        
            