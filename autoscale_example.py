# coding: utf-8
import boto3

session = boto3.Session(profile_name='craquiest')
as_client = session.client('autoscaling')

as_client.describe_auto_scaling_groups()
as_client.describe_policies()

#put_scaling_policy(**kwargs)  Creates or updates a scaling policy for an Auto Scaling group.

as_client.execute_policy( AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
as_client.execute_policy( AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Down')
