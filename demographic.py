import os, json, boto3

bucketName = os.environ.get('BUCKET_NAME')
output = "elections/projects/2020-election-results/demographic.json"

localFile = './data/demographic.json'

s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY_ID')
)
s3.upload_file(localFile, bucketName, output)
