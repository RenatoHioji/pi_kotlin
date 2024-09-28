from models.User import User
from repository.ItemRepository import ItemRepository
from sqlalchemy.exc import IntegrityError, NoResultFound
from uuid import UUID
class ItemService():
    def findAll():
        try:
            return ItemRepository.findAll()
        except Exception as e:
            return {"error": f"Não foi possível buscar os itens: {e}"}

        