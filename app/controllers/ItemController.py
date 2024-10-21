from flask import request, jsonify, abort
from service.ItemService import ItemService
class ItemController():
    def init_app(app):
        item_service = ItemService()
        @app.route("/item", methods=["GET"])
        def findAll():
            items = ItemService.findAll()

            return jsonify({"message": "Itens encontrados com sucesso", "items": items}), 200
        
        @app.route("/item", methods=["POST"])
        def save():
            data = request.form
            files = request.files
            if not data["name"] or data["syllables"]:
                abort(400, description="Um dos dados não foi enviado para a criação do item")
            if not 'image' in files or not 'video' in files:
                abort(400, description="Imagem ou video não enviados")
            if not data["category"] and data["subcategory"]:
                abort(400, description="Possui subcategoria, porém não há categoria")
                
            item_service.save(data["name"], data["syllables"], files["image"], files["video"], data["category"], data["subcategory"])
            return jsonify({"message" : "Item salvo com sucesso!"}), 201
