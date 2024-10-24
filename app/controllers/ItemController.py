from flask import request, jsonify, abort, session
from service.ItemService import ItemService
import uuid
from utils.id_converter import id_converter
class ItemController():
    def init_app(app):
        item_service = ItemService()
        @app.route("/item", methods=["GET"])
        def findAll():
            items = ItemService.findAll()
            return jsonify({"message": "Itens encontrados com sucesso", "items": items}), 200

        @app.route("/user/<string:id>/item", methods=["POST"])
        def saveItemToUser(id: str):
            user_id = id_converter.convert_id_uuid(id)
            data = request.form
            files = request.files
            if not data["name"] or not data["syllables"]:
                abort(400, description="Um dos dados não foi enviado para a criação do item")
            if not 'image' in files or not 'video' in files:
                abort(400, description="Imagem ou video não enviados")
            if not data["category"] and data["subcategory"]:
                abort(400, description="Possui subcategoria, porém não há categoria")
                
            item_service.saveItemToUser(data["name"], data["syllables"], files["image"], files["video"], data["category"], data["subcategory"], user_id)
            return jsonify({"message" : "Item salvo com sucesso!"}), 201    
        @app.route("/item", methods=["POST"])
        def save():
            data = request.form
            files = request.files
            if not data["name"] or not data["syllables"]:
                abort(400, description="Um dos dados não foi enviado para a criação do item")
            if not 'image' in files or not 'video' in files:
                abort(400, description="Imagem ou video não enviados")
            if not data["category"] and data["subcategory"]:
                abort(400, description="Possui subcategoria, porém não há categoria")
                
            item_service.save(data["name"], data["syllables"], files["image"], files["video"], data["category"], data["subcategory"])
            return jsonify({"message" : "Item salvo com sucesso!"}), 201
        
        @app.route("/item/<string:id>", methods=["DELETE"])
        def delete(id: str):
            item_id = id_converter.convert_id_uuid(id)
            item_service.delete(item_id)
            return jsonify({"message": "Item deletado com sucesso"}), 204
        @app.route("/item/<string:id>", methods=["GET"])
        def findById(id: str):
            item_id = id_converter.convert_id_uuid(id)
            item = item_service.findById(item_id)
            return jsonify({"message:": "Item buscado com sucesso", "item": item}), 200
        
        @app.route("/item/<string:id>", methods=["PUT"])
        def update(id: str):
            data = request.form
            files = request.files
            item_id = id_converter.convert_id_uuid(id)
            
            if not data["name"] or not data["syllables"]:
                abort(400, description="Um dos dados não foi enviado para a criação do item")
            if not 'image' in files or not 'video' in files:
                abort(400, description="Imagem ou video não enviados")
            if not data["category"] and data["subcategory"]:
                abort(400, description="Possui subcategoria, porém não há categoria")
                
            item_updated = item_service.update(item_id, data["name"], data["syllables"], files["image"], files["video"], data["category"], data["subcategory"])
            
            return jsonify({"message": "Item atualizado com sucesso", "item": item_updated})
        
