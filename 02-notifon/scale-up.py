import boto3

session = boto3.Session(profile_name='craquiest')
as_client = session.client('autoscaling')

as_client.execute_policy( AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
