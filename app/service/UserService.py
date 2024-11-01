from models.User import User
from repository.UserRepository import UserRepository
from repository.ItemRepository import ItemRepository
from utils.hash.password import verify_password
from flask import session, abort
from uuid import UUID
class UserService():
    def register(user: User):
        UserRepository.register(user)
    def login(user: User):
        userRegistered = UserRepository.findByEmail(user.email)
        if userRegistered and verify_password(userRegistered.password, user.password):
            session['user_id'] = userRegistered.id
            session['email'] = userRegistered.username
            return userRegistered
        else:
            abort(404, description = "Usuário email e/ou senhas incorretas ou usuário inexistente")
                
    def findUserById(user_id: UUID):
        user = UserRepository.findUserById(user_id)
        if not user:
            abort(404, description = "Usuário não foi encontrado")
        return user.get_profile()
    
    
    
    def updateUser(user: User, user_id: UUID):
        oldUser = UserRepository.findUserById(user_id)
        oldUser.email = user.email
        oldUser.password = user.password
        oldUser.username = user.username
        UserRepository.updateUser(oldUser)
        return 
    
    def delete(user_id: UUID):
        user = UserRepository.findUserById(user_id)
        return UserRepository.delete(user)

    def findUserItems(user_id):
        user = UserRepository.findUserById(user_id)
        if not user:
            abort(400, description="Usuário não encontrado")
        return user.get_items()
    
    def findUserHistory(user_id: UUID):
        history = UserRepository.findUserById(user_id).get_history()
        if not history:
            abort(404, description = "Histórico não foi encontrado")
        return history[::-1]
    
    def find_more_view_items(user_id: UUID):
        more_view = UserRepository.find_more_view_items(user_id)
        items = []
        for object in more_view:
            items.append(ItemRepository.findById(object[0]).serialize())
        if not more_view:
            abort(404, "Usuário ainda não viu nenhum item")
        return items