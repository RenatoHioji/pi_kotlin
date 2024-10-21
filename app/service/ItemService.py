from models.User import User
from repository.ItemRepository import ItemRepository
from sqlalchemy.exc import IntegrityError, NoResultFound
from uuid import UUID
from datetime import datetime
from PIL import Image
from werkzeug.utils import secure_filename
from flask import abort
from utils.s3 import bucket_pi_accessing
from models.Item import Item
import io
from schemas.ItemSchema import ItemSchema

class ItemService():
    def findAll():
        items = ItemRepository.findAll()
        item = ItemSchema(many=True)
        return item.jsonify(items)
    
    def save(self, name, syllables, img, video, category, subcategory):
        image_url, video_url =self.file_verification(img, video)
        item = Item(name, syllables, image_url, video_url, category, subcategory)
        return ItemRepository.save(item)
        
    def file_verification(self, image, video):
        if self.allowed_file(image.filename) and self.allowed_file(video.filename):
            image_name = self.convert_to_webp_and_save(image, secure_filename(image.filename))
            video_name = self.upload_video(video, secure_filename(video.filename))
            return image_name, video_name
        else:
            abort(400, description="Video ou imagem foi enviado com uma extensão proibída")
            
    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "mp3", "mp4"}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def convert_to_webp_and_save(self, image, filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name, extension = filename.rsplit('.', 1)
        img = Image.open(image)
        new_filename = f"{name}_{timestamp}.webp"
        buffer = io.BytesIO()
        if extension.lower() == "png":
            img.save(buffer, "webp", lossless=True)
        elif extension.lower() in ["jpg", "jpeg"]:
            img.save(buffer, "webp", quality=85)
        buffer.seek(0)
        bucket_pi_accessing.saveFile(buffer, new_filename)
        return new_filename
    
    def upload_video(self, video, original_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name, extension = original_filename.rsplit('.', 1)
        video_filename = f"{base_name}_{timestamp}.{extension}"
        buffer = io.BytesIO()
        buffer.write(video.read())
        buffer.seek(0)
        bucket_pi_accessing.saveFile(buffer, video_filename)
        return video_filename
                
