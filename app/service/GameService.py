import uuid
from uuid import UUID
from repository.GameRepository import GameRepository
from flask import abort
from models.Game import Game
class GameService:
    def findAll():
        games = GameRepository.findAll()
        return Game.serialize_list(games)
    def findById(id: UUID):
        game = GameRepository.findById(id)
        if not game:
            abort(404, description=f"Jogo não encontrado com id: {id}")
        return game.serialize()