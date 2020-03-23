import os


def post_to_slack(event, context):
    
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
    print(slack_webhook_url)
    print(event)
    return 

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
