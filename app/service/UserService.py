from models.User import User
from repository.UserRepository import UserRepository
from repository.ItemRepository import ItemRepository
from utils.hash.password import verify_password
from flask import session, abort
from uuid import UUID
import logging

logging.basicConfig(level=logging.DEBUG)

class UserService():
    def register(user: User):
        logging.info("Service - Register")
        UserRepository.register(user)
    def login(user: User):
        logging.info("Service - Login")
        userRegistered = UserRepository.find_by_email(user.email)
        if userRegistered and verify_password(userRegistered.password, user.password):
            session['user_id'] = userRegistered.id
            session['email'] = userRegistered.username
            return userRegistered
        else:
            abort(404, description = "Usuário email e/ou senhas incorretas ou usuário inexistente")
                
    def find_user_by_id(user_id: UUID):
        logging.info("Service - Find User By Id")
        
        user = UserRepository.find_user_by_id(user_id)
        if not user:
            abort(404, description = "Usuário não foi encontrado")
        return user.get_profile()
    
    
    
    def update_user(user: User, user_id: UUID):
        logging.info("Service - Update User")
        
        oldUser = UserRepository.find_user_by_id(user_id)
        oldUser.email = user.email
        oldUser.password = user.password
        oldUser.username = user.username
        UserRepository.update_user(oldUser)
        return 
    
    def delete(user_id: UUID):
        logging.info("Service - Delete User")
        user = UserRepository.find_user_by_id(user_id)
        return UserRepository.delete(user)

    def find_user_items(user_id):
        logging.info("Service - Find user itens")
        user = UserRepository.find_user_by_id(user_id)
        if not user:
            abort(400, description="Usuário não encontrado")
        return user.get_items()
    
    def find_user_history(user_id: UUID):
        logging.info("Service - Find User History")
        history = UserRepository.find_user_by_id(user_id).get_history()
        if not history:
            abort(404, description = "Histórico não foi encontrado")
        return history[::-1]
    
    def find_more_view_items(user_id: UUID):
        logging.info("Service - Find omre viewed itens")
        more_view = UserRepository.find_more_view_items(user_id)
        items = []
        for object in more_view:
            items.append(UserRepository.find_user_by_id(object[0]).serialize())
        if not more_view:
            abort(404, "Usuário ainda não viu nenhum item")
        return items