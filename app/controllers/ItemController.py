from flask import request, jsonify, abort, session
from service.ItemService import ItemService
import uuid
import logging
from utils.verification import Verificator
from utils.id_converter import id_converter

logging.basicConfig(level=logging.DEBUG)

class ItemController():
    
    def init_app(app):
        item_service = ItemService()
        @app.route("/item", methods = ["GET"])
        def find_items_by_params():
            category = request.args.get("category") 
            subcategory = request.args.get("subcategory") 
            items = ItemService.find_by_params(category, subcategory)
            return jsonify({"message": "Itens encontrados com sucesso", "items": items})
        @app.route("/items", methods=["GET"])
        def find_all():
            items = ItemService.find_all()
            return jsonify({"message": "Itens encontrados com sucesso", "items": items}), 200
        @app.route("/user/<string:id>/item", methods=["POST"])
        def save_item_to_user(id: str):
            user_id = id_converter.convert_id_uuid(id)
            data = request.form
            Verificator.verify(data)
            item_service.save_item_to_user(data["name"], data["syllables"], data["image"], data["video"], data["videoName"],data["audio"], data["category"], data["subcategory"], user_id)
            return jsonify({"message" : "Item salvo com sucesso!"}), 201    
        @app.route("/item", methods=["POST"])
        def save():
            data = request.form
            Verificator.verify(data)
                
            item_service.save(data["name"], data["syllables"], data["image"], data["video"], data["videoName"], data["audio"], data["category"], data["subcategory"])
            return jsonify({"message" : "Item salvo com sucesso!"}), 201
        
        @app.route("/item/<string:id>", methods=["DELETE"])
        def delete(id: str):
            item_id = id_converter.convert_id_uuid(id)
            item_service.delete(item_id)
            return jsonify({"message": "Item deletado com sucesso"}), 204
        @app.route("/item/<string:id>/user/<string:id_user>", methods=["GET"])
        def find_by_id(id: str, id_user: str):
            item_id = id_converter.convert_id_uuid(id)
            user_id = id_converter.convert_id_uuid(id_user)
            item = item_service.find_by_id(item_id, user_id)
            return jsonify({"message:": "Item buscado com sucesso", "item": item}), 200
        
        @app.route("/item/<string:id>", methods=["PUT"])
        def update(id: str):
            data = request.form
            item_id = id_converter.convert_id_uuid(id)
            Verificator.verify(data)
            item_updated = item_service.update(item_id, data["name"], data["syllables"], data["image"], data["video"], data["videoName"], data["audio"], data["category"], data["subcategory"])
            
            return jsonify({"message": "Item atualizado com sucesso", "item": item_updated})
        
