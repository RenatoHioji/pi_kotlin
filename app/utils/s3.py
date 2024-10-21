import boto3
import os
import boto3.exceptions
from botocore.exceptions import ClientError
from flask import abort
class bucket_pi_accessing:
    @staticmethod
    def saveFile(file, new_filename):
        try:
            s3 = boto3.resource("s3")
            response = s3.Bucket(os.environ.get("BUCKET_NAME")).upload_fileobj(file, new_filename)
            print(response)
        except boto3.exceptions.S3UploadFailedError as e:
            abort(500, description=f"Erro ao tentar o arquivo na nuvem: {file}")
    
    def deleteFile(filename):
        try: 
            s3 = boto3.resource("s3")
            response = s3.delete_object(Bucket=os.environ.get("BUCKET_NAME", Key=filename))
        except ClientError as e:
            abort(500, description=f"Erro ao deletar arquivo na nuvem: {filename}")
            
        
