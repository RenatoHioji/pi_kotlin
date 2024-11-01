from flask import request, jsonify, abort, session
from service.ItemService import ItemService
import uuid
from utils.id_converter import id_converter
class ItemController():
    def init_app(app):
        game_service = GameService()
        @app.route("/game", methods=["GET"])
        def findAll():
            games = ItemService.findAll()
            return jsonify({"message": "Itens encontrados com sucesso", "games": games}), 200
        @app.route("/game/<string:id>", methods=["GET"])
        def findById(id: str):
            game_id = id_converter.convert_id_uuid(id)
            game = game_service.findById(item_id)
            return jsonify({"message:": "Item buscado com sucesso", "game": game}), 200