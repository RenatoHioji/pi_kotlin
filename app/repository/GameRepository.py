from models.Game import Game
from uuid import UUID
class GameRepository:
    def findAll():
        return Game.query.all()

    def findById(id: UUID):
        return Game.query.filter_by(id=id).first()

    