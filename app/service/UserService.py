from models.User import User

class UserService():
    def register(user: User):
        try:
            UserRepository.register(user)
        except OperationalError as e:
            print(e)
            