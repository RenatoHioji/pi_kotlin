from models.User import User

class UserService():
    def register(user: User):
        try:
            UserRepository.register(user)
        catch(e):
            