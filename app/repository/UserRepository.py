from models.db import db
from models.User import User
from sqlalchemy.exc import IntegrityError
from flask import abort
from uuid import UUID
import uuid

class UserRepository():
    def register(user: User):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError as e:
            db.session.rollback() 
            abort(500, description = "Usuário já cadastrado")
        except Exception as e:
            db.session.rollback() 
            abort(500, description = f"Exception: {e}")
        
    def findByEmail(email: str):
        try:
            user = User.query.filter_by(email = email).first()
            if not user:
                abort(404, description = "Usuário não foi encontrado")
        except Exception as e:
            abort(500, description=f"Erro na query: {e}")
        return user
    
    def findUserHistory(user_id: UUID):
        try:
            history = User.query.filter_by(id = user_id).first()
            print(history)
            return history
        except Exception as e:
            abort(500, description = f"Erro na query: {e}")