from models.Item import Item
from uuid import UUID
class ItemRepository():
    def findAll():
        try:
            return Item.query.all()
        except Exception as e:
            print("exception: ", e)
            raise