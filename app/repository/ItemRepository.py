from models.Item import Item
from uuid import UUID
from flask import abort
from sqlalchemy.exc import SQLAlchemyError
class ItemRepository():
    def findAll():
        try:
            item = Item.query.all()
            if not item:
                abort(404, description = "Não foi possível encontrar um item")
        except SQLAlchemyError as e:
            abort(500, description= f"falha na query: {e}")
    
            