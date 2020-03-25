# coding: utf-8
import json

event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:eu-west-2:020400783804:handleLabelDetectionTopic:d866fc6b-a98b-44e4-b49f-377e5a271f57', 'Sns': {'Type': 'Notification', 'MessageId': '8edcfea3-188b-5784-b17c-a85680e00e63', 'TopicArn': 'arn:aws:sns:eu-west-2:020400783804:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"8d258ea7ef27275ad7f75bca24dd97eabd3bb91a27fc9d580584c89a04893c31","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1585157674661,"Video":{"S3ObjectName":"womanphone.mp4","S3Bucket":"craquiestvideolyzer"}}', 'Timestamp': '2020-03-25T17:34:35.185Z', 'SignatureVersion': '1', 'Signature': 'KXutJKxGXP/6a6jYZqR++MhGLTuGD4oDa0B1i6sx2BWRPIatBUwIiT0XzByqsYD70VSs0Uiv7nPN4c70pH0R5FbTkExA8Xzzcmu6iFEt2HkQKilBA5eUJioSrVEjAMmZ4q5A8MwfnB98zxb1jHinPgDeojYtCD/HdmMFvhqgk9M7F3cusA8x50u+FlRIFXKOPy+/6mxgA30pn7NE4YhryfKHo1e5l9a4XMQOYVGASgxIJjxRAHBqfnsf60LJLDsfQ9e4zK0IsnRPmRuD7y7ErI8zYKR794EpvK8RZKiqGmoJtphNp8TFkAyWpdEhShRDdsVWkNrjpeTowY1h1uRGEQ==', 'SigningCertUrl': 'https://sns.eu-west-2.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 'UnsubscribeUrl': 'https://sns.eu-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-2:020400783804:handleLabelDetectionTopic:d866fc6b-a98b-44e4-b49f-377e5a271f57', 'MessageAttributes': {}}}]}

event
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']['JobId']

type(event['Records'][0]['Sns']['Message'])
json.loads(event['Records'][0]['Sns']['Message'])
