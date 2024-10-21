import boto3
import os
from flask import abort
class bucket_pi_accessing:
    @staticmethod
    def saveFile(file, new_filename):
        try:
            s3 = boto3.resource("s3")
            s3.Bucket(os.environ.get("BUCKET_NAME")).upload_fileobj(file, new_filename)
        except boto3.exceptions.S3UploadFailedError as e:
            abort(500, f"Erro ao tentar o arquivo no banco de dados: {file}")
        
        
