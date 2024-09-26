from flask import request, jsonify, abort, session
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.ItemService import ItemService
from sqlalchemy.exc import IntegrityError
from uuid import UUID

class ItemController():
    def init_app(app):
        route = "item"
        @app.route(f"/{route}", methods=["GET"])
        def findAllItems():
            items = ItemService.findAll()
            if 'error' in items:
                return jsonify(
                    items
                ), 500
            return jsonify({"message": "Itens encontrados com sucesso", "items": items}), 200
        
        @app.route(f"/{route}/recents/<uuid:user_id>", methods=["GET"])
        def findRecents(user_id: UUID):
            if not user_id:
                return jsonify({"error": "Id de usuário não foi enviado"}), 400
            
            history = ItemService.findRecents(user_id)
            if 'error' in history:
                return jsonify(
                    history
                ), 500
            return jsonify({"message": "Histórico de itens encontrados com sucesso", "items": history}), 200
        