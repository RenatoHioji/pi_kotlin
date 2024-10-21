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
            if not 'image' in files or not 'video' in files:
                abort(400, description="Imagem ou video não enviados")
            item_service.save(data["name"], data["syllables"], files["image"], files["video"], data["category"], data["subcategory"])
            return jsonify({"message" : "Item salvo com sucesso!"}), 201
