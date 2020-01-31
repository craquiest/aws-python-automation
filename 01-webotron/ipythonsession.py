# coding: utf-8
import boto3
session = boto3.Session(profile_name='craquiest')
s3 = session.resource('s3')
# get_ipython().run_line_magic('history', '')
# new_bucket = s3.create_bucket(Bucket='aws-python-automation-alg', CreateBucketConfiguration={
#         'LocationConstraint': 'eu-west-2'})
# for bucket in s3.buckets.all(): print(bucket)
# ec2_client = session.client('ec2')
