from models.Game import Game
from uuid import UUID
class GameRepository:
    def find_all():
        return Game.query.all()

    def find_by_id(id: UUID):
        return Game.query.filter_by(id=id).first()

    