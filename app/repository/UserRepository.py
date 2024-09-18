from models.db import db
from models.User import User
from sqlalchemy.exc import IntegrityError
from flask import jsonify

class UserRepository():
    def register(user: User):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError as e:
            print("exception")
            db.session.rollback() 
            raise
        except Exception as e:
            db.session.rollback() 
            print("exception")
            raise
    def findByEmail(email: str):
        user = User.query.filter_by(email = email).first()
        return user
    