# coding: utf-8
import boto3

event= {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'eu-west-2', 'eventTime': '2020-03-24T19:02:14.808Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAQJP73IG6K2FV6CBRT'}, 'requestParameters': {'sourceIPAddress': '82.47.123.146'}, 'responseElements': {'x-amz-request-id': '3EC4DC6389CFEC9E', 'x-amz-id-2': 'L6IGlUsGaV8/RtPdYty2jguI8EiMaRar249qSV812VL5dk4dzkc2uVkIpgmjJP/fg7OZyc6NL/FLeo2VK6N1YFuwX1XDDWeJ'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '40556e6f-7564-4d62-a4e7-6c5cea1ad90a', 'bucket': {'name': 'craquiestvideolyzer', 'ownerIdentity': {'principalId': 'A1KU6WLQB1W2QZ'}, 'arn': 'arn:aws:s3:::craquiestvideolyzer'}, 'object': {'key': 'video.mp4', 'size': 24442740, 'eTag': '62258b11cc7c0e749ec8d30b1b111e66-3', 'sequencer': '005E7A5933396A2A01'}}}]}

event
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']

import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
