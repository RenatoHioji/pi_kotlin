from flask import request, jsonify, abort, session
from service.GameService import GameService
import uuid
from utils.id_converter import id_converter
class GameController():
    def init_app(app):
        @app.route("/game", methods=["GET"])
        def findAllGames():
            games = GameService.findAll()
            return jsonify({"message": "Itens encontrados com sucesso", "games": games}), 200
        @app.route("/game/<string:id>", methods=["GET"])
        def findByGameId(id: str):
            game_id = id_converter.convert_id_uuid(id)
            game = GameService.findById(game_id)
            return jsonify({"message:": "Item buscado com sucesso", "game": game}), 200