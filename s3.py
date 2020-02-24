import os, json
import boto3

bucketName = os.environ.get('BUCKET_NAME')
wireOutput = "elections/projects/2020-election-results/wire.json"
localOutput = "elections/projects/2020-election-results/local.json"

wireFile = './data/wire.json'
localFile = './data/local.json'

s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY_ID')
)
s3.upload_file(wireFile, bucketName, wireOutput)
s3.upload_file(localFile, bucketName, localOutput)
