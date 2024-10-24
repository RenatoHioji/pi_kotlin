import os
import boto3.exceptions
import boto3
from flask import abort
from botocore.exceptions import ClientError
class bucket_pi_accessing:
    @staticmethod
    def init_s3():
        try:
            global s3Bucket
            s3 = boto3.resource("s3")
            s3Bucket = s3.Bucket(os.environ.get("BUCKET_NAME"))
            print("S3 Inicializado com sucesso")
        except Exception as e:
            print("Não foi possíevl inicializar o S3 client")

    @staticmethod
    def saveFile(file, new_filename):
        try:
            s3Bucket.upload_fileobj(file, new_filename)
        except boto3.exceptions.S3UploadFailedError as e:
            abort(500, description=f"Erro ao tentar o arquivo na nuvem: {file}")
    
    @staticmethod
    def deleteFile(filename):
        try: 
            response = s3Bucket.delete_objects(Delete={'Objects': [{'Key': filename}]})
            print(response)
        except ClientError as e:
            abort(500, description=f"Erro ao deletar arquivo na nuvem: {filename}")