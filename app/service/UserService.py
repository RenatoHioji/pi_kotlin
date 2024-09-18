from models.User import User
from repository.UserRepository import UserRepository
from sqlalchemy.exc import IntegrityError
class UserService():
    def register(user: User):
        try:
            UserRepository.register(user)
            return {"message": "Usuário cadastrado com sucesso"}
        except IntegrityError as e:
            return {"error": "Usuário com esse email ou senha já existe"}
        
        except Exception as e:
            return {"error": f"{e}"}
        
            