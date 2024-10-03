from flask import request, jsonify, abort, session
from utils.hash.password import hash_password, verify_password
from models.User import User
from service.ItemService import ItemService
from sqlalchemy.exc import IntegrityError
import uuid

class ItemController():
    def init_app(app):
        @app.route("/item", methods=["GET"])
        def findAll():
            items = ItemService.findAll()
            return jsonify({"message": "Itens encontrados com sucesso", "items": items}), 200
        
        @app.route("/item", methods=["POST"])
        def save():
            data = request.get_json()
            files = request.files
            
            if 'image' not in files:
                abort(404, description="Imagem não foi enviada.")
            if 'video' not in files:
                abort(404, description = "Vídeo não foi enviado.")
            
            return jsonify("message": "Arquivos enviados com sucesso!")