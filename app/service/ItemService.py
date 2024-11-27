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
from utils.file_converter import FileConverter

class ItemService:
    def find_all():
        items = ItemRepository.find_all()
        return Item.serialize_list(items)

    def save_item_to_user(self, name, syllables, image, video, video_name, audio, category, subcategory, user_id):
        converted_img = FileConverter.convert_blob_to_image(image)
        converted_audio = FileConverter.convert_blob_to_audio(audio)
        converted_video = FileConverter.convert_blob_to_mp4(video, video_name)
        image_url, video_url, audio_url = self.file_verification(converted_img, converted_video, converted_audio)
        item = Item(name, syllables, image_url, video_url, audio_url, category, subcategory, user_id)
        return ItemRepository.save(item)

    def save(self, name, syllables, image, video, video_name, audio, category, subcategory):
    converted_img = FileConverter.convert_blob_to_image(image)
        converted_audio = FileConverter.convert_blob_to_audio(audio)
        converted_video = FileConverter.convert_blob_to_mp4(video, video_name)
        image_url, video_url, audio_url = self.file_verification(converted_img, converted_video, converted_audio)
        item = Item(name, syllables, image_url, video_url, audio_url, category, subcategory)
        return ItemRepository.save(item)

    def delete(self, id: UUID):
        item = ItemRepository.find_by_id(id)
        bucket_pi_accessing.delete_file(item.img)
        bucket_pi_accessing.delete_file(item.video)
        bucket_pi_accessing.delete_file(item.audio)
        ItemRepository.delete(item)

    def find_by_id(self, id: UUID, user_id: UUID):
        item = ItemRepository.find_by_id(id)
        ItemRepository.add_user_history(id, user_id)
        return item.serialize()

    def find_by_params(category=None, subcategory=None):
        filters = []
        if category:
            filters.append(Item.category == category)
        if subcategory:
            filters.append(Item.subcategory == subcategory)

        items = ItemRepository.find_by_params(filters)
        if not items:
            abort(404, description=f"Não foi encontrado nenhum item com a categoria: {category} e/ou subcategoria: {subcategory}")

        return Item.serialize_list(items)

    def update(self, id: UUID, name, syllables, image, video, video_name, audio, category, subcategory):
        old_item = ItemRepository.find_by_id(id)
        bucket_pi_accessing.delete_file(old_item.img)
        bucket_pi_accessing.delete_file(old_item.video)
        bucket_pi_accessing.delete_file(old_item.audio)
        converted_img = FileConverter.convert_blob_to_image(image)
        converted_audio = FileConverter.convert_blob_to_audio(audio)
        converted_video = FileConverter.convert_blob_to_mp4(video, name)

        image_url, video_url, audio_url = self.file_verification(converted_image, converted_video, converted_audio)

        old_item.name = name
        old_item.syllables = syllables
        old_item.img = image_url
        old_item.video = video_url
        old_item.audio = audio_url
        old_item.category = category
        old_item.subcategory = subcategory

        ItemRepository.update(old_item)

        return old_item.serialize()

    def file_verification(self, image, video, audio):
        if self.allowed_file(image.filename) and self.allowed_file(video.filename) and self.allowed_file(audio.filename):
            image_name = self.convert_to_webp_and_save(image, secure_filename(image.filename))
            video_name = self.upload_video(video, secure_filename(video.filename))
            audio_name = self.upload_audio(audio, secure_filename(audio.filename))
            return image_name, video_name, audio_name
        else:
            abort(400, description="Video ou imagem foi enviado com uma extensão proibída")

    @staticmethod
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "jfif", "mp3", "mp4"}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def convert_to_webp_and_save(self, image, filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name, extension = filename.rsplit('.', 1)
        img = Image.open(image)
        new_filename = f"{name}_{timestamp}.webp"
        buffer = io.BytesIO()
        if extension.lower() == "png":
            img.save(buffer, "webp", lossless=True)
        elif extension.lower() in ["jpg", "jpeg", "jfif"]:
            img.save(buffer, "webp", quality=85)
        buffer.seek(0)
        bucket_pi_accessing.save_file(buffer, new_filename)
        return new_filename

    def upload_video(self, video, original_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name, extension = original_filename.rsplit('.', 1)
        video_filename = f"{base_name}_{timestamp}.{extension}"
        buffer = io.BytesIO()
        buffer.write(video.read())
        buffer.seek(0)
        bucket_pi_accessing.save_file(buffer, video_filename)
        return video_filename

    def upload_audio(self, audio, original_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name, extension = original_filename.rsplit('.', 1)
        audio_filename = f"{base_name}_{timestamp}.{extension}"
        buffer = io.BytesIO()
        buffer.write(audio.read())
        buffer.seek(0)
        bucket_pi_accessing.save_file(buffer, audio_filename)
        return audio_filename
