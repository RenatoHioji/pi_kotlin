from models.db import db
from models.User import User
from sqlalchemy.exc import IntegrityError
from flask import abort
from uuid import UUID
import uuid
from sqlalchemy.exc import SQLAlchemyError

class UserRepository():
    def register(user: User):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError as e:
            db.session.rollback() 
            abort(500, description = "Usuário já cadastrado")
        except SQLAlchemyError as e:
            db.session.rollback() 
            abort(500, description = f"Exception: {e}")
        
    def findByEmail(email: str):
        try:
            user = User.query.filter_by(email = email).first()
            if not user:
                abort(404, description = "Usuário não foi encontrado")
        except SQLAlchemyError as e:
            abort(500, description=f"Erro na query: {e}")
        return user
    
    def findUserById(user_id: UUID):
        try:
            history = User.query.filter_by(id = user_id).first()
            return history
        except SQLAlchemyError as e:
            abort(500, description = f"Erro na query: {e}")
    
    def updateUser(user: User):
        try:
            db.session.commit()
            return
        except IntegrityError as e:
            db.session.rollback() 
            abort(500, description = "Usuário já cadastrado")
        except SQLAlchemyError as e:
            abort(500, description = f"Erro na query: {e}")
    def delete(user: User):
        try:
            db.session.delete(user)
            db.session.commit()
            return
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description = f"Erro na query: {e}")