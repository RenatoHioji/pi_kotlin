from models.Item import Item
from uuid import UUID
class ItemRepository():
    def findAll():
        try:
            return Item.query.all()
        except Exception as e:
            print("exception: ", e)
            raise
    def findRecents(user_id: UUID):
        try:
            return History.query.filter_by(user_id=user_id)
        except Exception as e:
            print("Exception: ", e)
            raise