# coding: utf-8
from pathlib import Path
import boto3

session = boto3.Session(profile_name='craquiest')
session.region_name

s3 = session.resource('s3')
bucket = s3.create_bucket(
    Bucket='craquiestvideolyzer',
    CreateBucketConfiguration={'LocationConstraint': session.region_name}
)
list(s3.buckets.all())

# get_ipython().run_line_magic('ls', '/Users/Lamine/Downloads/*.mp4')
pathname = '/Users/Lamine/Downloads/Pexels Videos 1526909.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
str(path)
path.name

bucket.upload_file(str(path), str(path.name))
list(bucket.objects.all())

rekognition_client = session.client('rekognition')

response = rekognition_client.start_label_detection(
                Video={'S3Object': {
                            'Bucket': bucket.name, 
                            'Name': path.name
                            }
                    })
response
job_id = response['JobId']

result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
