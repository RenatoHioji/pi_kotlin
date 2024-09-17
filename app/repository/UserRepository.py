from models.User import User
class UserRepository():
    def register(user: User):
        return await user.save()

    def findById(id: int):
        return await user.filter()
        