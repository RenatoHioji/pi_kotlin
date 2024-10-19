
s3 = boto3.resource("s3")
bucket_name = "tagarela-sunside-pi-dsm"
s3.Bucket(bucket_name).upload_fileobj(uploaded_file, new_filename)