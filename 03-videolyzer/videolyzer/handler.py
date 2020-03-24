import urllib

import boto3

def start_label_detection(bucket, key):
    """Util function called by triggered lambda function.
    Start the label detection process in Rekognition 
    when given access to file via bucket & key """

    rekognition_client = boto3.client('rekognition')
    # notice we don't use a session as lambda executes through its own permissions

    response = rekognition_client.start_label_detection(
                Video={'S3Object': {
                            'Bucket': bucket, 
                            'Name': key
                            }
                    })
    print(response)

    return


def start_processing_video(event, context):
    """Lambda event handler for Rekognition"""
    # event['Records'] contains a list of records (for each video uploaded)
    for record in event['Records']:
        start_label_detection(
            record['s3']['bucket']['name'],
            urllib.parse.unquote_plus(record['s3']['object']['key'])
        )

    return
