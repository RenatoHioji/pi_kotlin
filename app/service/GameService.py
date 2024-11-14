import uuid
from uuid import UUID
from repository.GameRepository import GameRepository
from flask import abort
from models.Game import Game
import logging
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)
class GameService:
    def find_all():
        games = GameRepository.find_all()
        return Game.serialize_list(games)
    def find_by_id(id: UUID):
        logger.info(id)
        game = GameRepository.find_by_id(id)
        if not game:
            abort(404, description=f"Jogo não encontrado com id: {id}")
        return game.serialize()