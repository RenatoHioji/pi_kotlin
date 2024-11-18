from models.db import db, user_history
from models.User import User
from sqlalchemy.exc import IntegrityError
from flask import abort
from uuid import UUID
import uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
class UserRepository():
    def register(user: User):
        try:
            db.session.add(user)
            db.session.commit()
            return User.query.filter_by(email = user.email).first()
        except IntegrityError as e:
            db.session.rollback() 
            abort(500, description = "Usuário já cadastrado")
        except SQLAlchemyError as e:
            db.session.rollback() 
            abort(500, description = f"Exception: {e}")
        
    def find_by_email(email: str):
        try:
            user = User.query.filter_by(email = email).first()
            if not user:
                abort(404, description = "Usuário não foi encontrado")
            return user
        except SQLAlchemyError as e:
            abort(500, description=f"Erro na query: {e}")
    
    def find_user_by_id(user_id: UUID):
        try:
            history = User.query.filter_by(id = user_id).first()
            return history
        except SQLAlchemyError as e:
            abort(500, description = f"Erro na query: {e}")
    
    def update_user(user: User):
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
            
    def find_more_view_items(user_id):
        try: 
            top_items = db.session.query(
                user_history.c.item_id,
                func.count(user_history.c.item_id).label('total')
            ).filter(
                user_history.c.user_id == user_id
            ).group_by(
                user_history.c.item_id
            ).order_by(
                func.count(user_history.c.item_id).desc()
            ).limit(10).all()
            return top_items
        except SQLAlchemyError as e:
            abort(500, description = f"Erro na query: {e}")
    