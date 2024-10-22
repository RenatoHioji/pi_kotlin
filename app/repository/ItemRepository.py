from models.Item import Item
from uuid import UUID
from flask import abort
from sqlalchemy.exc import SQLAlchemyError
from models.db import db
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