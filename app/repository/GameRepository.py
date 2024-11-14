from models.Game import Game
from uuid import UUID
import logging
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)
class GameRepository:
    def find_all():
        return Game.query.all()

    def find_by_id(id: UUID):
        logger.info(id)
        return Game.query.filter_by(id=id).first()

    