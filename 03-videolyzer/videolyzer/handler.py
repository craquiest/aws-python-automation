import os
import urllib
import boto3
import json

#! Helper functions

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
                    },
                NotificationChannel={
                    'SNSTopicArn': os.environ['REKOGNITION_SNS_TOPIC_ARN'],
                    'RoleArn': os.environ['REKOGNITION_ROLE_ARN']
                    }
                )
    print(response)

    return

def get_video_labels(job_id):
    rekognition_client = boto3.client('rekognition')

    response = rekognition_client.get_label_detection(JobId=job_id)

    next_token = response.get('NextToken', None)

    while next_token:
        next_page = rekognition_client.get_label_detection(
            next_page=job_id,
            NextToken=next_token
        )
        # Use extend i.o. append as add more than one element to the list
        response['Labels'].extend(next_page['Labels']) 

        next_token = next_page.get('NextToken', None)

    return response


def put_labels_in_db(data, video_name, video_bucket):

    pass

#! Lambda Events

def start_processing_video(event, context):
    """Lambda event handler for Rekognition"""
    # event['Records'] contains a list of records (for each video uploaded)
    for record in event['Records']:
        start_label_detection(
            record['s3']['bucket']['name'],
            urllib.parse.unquote_plus(record['s3']['object']['key'])
        )

    return


def handle_label_detection(event, context):

    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        job_id = message['JobId']
        s3_object = message['Video']['S3ObjectName']
        s3_bucket = message['Video']['S3Bucket']

        response = get_video_labels(job_id)
        print(response)
        put_labels_in_db(response, s3_object, s3_bucket)

    return