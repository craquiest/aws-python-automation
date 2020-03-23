# coding: utf-8
import boto3
session = boto3.Session(profile_name='craquiest')
ec2 = session.resource('ec2')

#! Create key pair
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
# get_ipython().run_line_magic('ls', '-l python_automation_key.pem')

#! Get the right image, filtering by image name and Owner
ec2.images.filter(Owners=['amazon'])
ami_list = list(ec2.images.filter(Owners=['amazon']))
len(ami_list)
img = ec2.Image('ami-0cb790308f7591fa6')
img.name

ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2') # this wont work
img_apse2 = ec2_apse2.Image('ami-0cb790308f7591fa6') # this wont work
img_apse2.name # this wont work

ami_name = img.name
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters = filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters = filters))

#! Create instances with ID, InstanceTyp and KeyName
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)

instances
ec2.Instance(id='i-0fc6e2e32ce9c9ebf')
inst = instances[0]
inst
inst.terminate()

instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)

inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()   #*Reload python object to make sure instance in there
inst.public_dns_name

#!  Security groups settings 
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '82.47.123.146/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
