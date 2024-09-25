from models.Item import Item

class ItemRepository():
    def findAll():
        try:
            return Item.query.all()
        except Exception as e:
            print("exception: ", e)
            raise
    