import boto3
import json
import logging
from urllib.parse import unquote_plus

bucketname = <bucket_name>
filename = "report.log"


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    added_file = unquote_plus(event['Records'][0]['s3']['object']['key'])
    upload_path = '/tmp/' + filename

    with open(upload_path, 'w+') as f:
        f.write(added_file)
    s3.upload_file(upload_path, bucketname, filename)
    msg = 'File ' + added_file + ' has been added!'
    logger.info(msg)
    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }

