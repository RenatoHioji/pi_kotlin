from models.User import User
from repository.ItemRepository import ItemRepository
from sqlalchemy.exc import IntegrityError, NoResultFound
from uuid import UUID
class ItemService():
    def findAll():
        return ItemRepository.findAll()