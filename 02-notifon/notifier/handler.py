import json


def hello(event, context):
    print(event)
    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }

    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response
