from flask import request, jsonify, abort, session
from service.ItemService import ItemService
from werkzeug.utils import secure_filename
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
            image = files['image']
            video = files['video']
            
            if allowed_file(image.filename) and allowed_file(video.filename):
                filename = secure_filename(image.filename)
                files['image'].save(os.path.join(app.config['UPLOAD_IMAGE'], filename))
                
                filename = secure_filename(video.filename)
                files['video'].save(os.path.join(app.config['UPLOAD_VIDEO'], filename))
            return jsonify({"message" : "Arquivos enviados com sucesso!"})
        
        def allowed_file(filename):
            ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "mp3", "mp4"}
            return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        