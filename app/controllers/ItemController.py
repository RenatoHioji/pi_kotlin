from flask import request, jsonify, abort, session
from service.ItemService import ItemService
from werkzeug.utils import secure_filename
import uuid
import os
from datetime import datetime
from PIL import Image

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
                convert_to_web_and_save(image, secure_filename(image.filename))
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                video_filename = f"{secure_filename(video.filename).rsplit('.', 1)[0]}_{timestamp}.{secure_filename(video.filename).rsplit('.', 1)[1]}"
                files['video'].save(os.path.join(app.config['UPLOAD_VIDEO'], video_filename))
            else:
                abort(400, "Video ou imagem foi enviado com uma extensão proibída")
                
            return jsonify({"message" : "Arquivos enviados com sucesso!"})
        
        def allowed_file(filename):
            ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "mp3", "mp4"}
            return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        
        def convert_to_web_and_save(image, filename):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            name, extension = filename.rsplit('.', 1)
            img = Image.open(image)
            new_filename = f"{name}_{timestamp}.webp"
            if extension == "png":
                img.save(os.path.join(app.config['UPLOAD_IMAGE'], new_filename, "webp", lossless=True))
            elif extension == "jpg" or extension == "jpeg":
                img.save(os.path.join(app.config['UPLOAD_IMAGE'], new_filename, "webp", quality=85))
                
            