import os

import requests

def post_to_slack(event, context):
    
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
    
    slack_message = "From {source} at {detail[StartTime]}: {detail[Description]}".format(**event)
    data = {"text": slack_message}
    requests.post(slack_webhook_url, json=data)

    # print(slack_webhook_url)
    # print(event)
    
    return 

# requests==2.18.4
# sodapy==1.4.6


# def  hello(event, context):
    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response
