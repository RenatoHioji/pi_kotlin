from models.User import User
from repository.ItemRepository import ItemRepository
from sqlalchemy.exc import IntegrityError, NoResultFound
class ItemService():
    def findAll():
        try:
            return ItemRepository.findAll()
        except Exception as e:
            return {"error": "Não foi possível buscar os itens"}
                     
        
            