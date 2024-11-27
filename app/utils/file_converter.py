import io
import ffmpeg
from moviepy.video.io import VideoFileClip
from pydub import AudioSegment
from PIL import Image

class FileConverter:
    @staticmethod
    def convert_blob_to_mp4(video_blob, file_name):
        video_file = io.BytesIO(video_blob)
        clip = VideoFileClip(video_file)
        clip = clip.set_fps(60)
        output_buffer = io.BytesIO()
        temp_file = f'{file_name}.mp4'
        clip.write_videofile(temp_file, codec='libx264', preset='ultrafast')
        (
            ffmpeg
            .input(temp_file)
            .output(output_buffer, format='mp4')
            .run(overwrite_output=True)
        )
        output_buffer.seek(0)
        return output_buffer

    @staticmethod
    def convert_blob_to_image(image_blob):
        image_file = io.BytesIO(image_blob)
        image = Image.open(image_file)
        image_format = image.format.lower()
        output_buffer = io.BytesIO()
        image.save(output_buffer, format=image_format)
        output_buffer.seek(0)
        return output_buffer

    @staticmethod
    def convert_blob_to_audio(blob, format='mp3'):
        audio_file = io.BytesIO(blob)
        audio = AudioSegment.from_file(audio_file, format=format)
        output_buffer = io.BytesIO()
        audio.export(output_buffer, format=format)
        output_buffer.seek(0)
        return output_buffer
