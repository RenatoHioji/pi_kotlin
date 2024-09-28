from flask import request, jsonify, abort, session
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.ItemService import ItemService
from sqlalchemy.exc import IntegrityError
import uuid

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
        
