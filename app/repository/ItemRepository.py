from models.Item import Item
from uuid import UUID
from flask import abort
from sqlalchemy.exc import SQLAlchemyError
from models.db import db, user_history

class ItemRepository():
    def findAll():
        try:
            items = Item.query.all()
            if not items:
                abort(404, description = "Não foi possível encontrar um item")
            return items
        except SQLAlchemyError as e:
            abort(500, description= f"falha na query: {e}")
    def save(item: Item):
        db.session.add(item)
        db.session.commit()
        return item
    
    def findById(id: UUID):
        item = Item.query.filter_by(id=id).first()
        if not item:
            abort(404, description="Item com o ID informado não foi encontrado")
        return item
    
    def findByParams(filters):
        items = Item.query.filter(*filters).all()
        return items
    
    def delete(item: Item):
        try:
            db.session.delete(item)
            db.session.commit()
            return
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description = f"Erro na query: {e}")
    
    def update(item: Item):
        try:
            db.session.commit()
            return
        except SQLAlchemyError as e:
            abort(500, description = f"Erro na query: {e}")
    def addUserHistory(item_id, user_id):
        db.session.execute(
            user_history.insert().values(user_id=user_id, item_id=item_id)
        )
        db.session.commit()