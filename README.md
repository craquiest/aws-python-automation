# Automating AWS with Python

Repository for Automating AWS with Python. ACG course

## 01-webotron

Webotron is a script that will sync a local directory to an S3 bucket, 
and optionally configure Route53 and CloudFront as well. 

### Features

Webotron currently has the following features:

- List buckets
- List contents of a bucket
- Create and setup bucket (policy, website and error-handling)
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName> as command line option through click
- Configure route 53 domain


## 02-notifon

Notifon is a project to notify Slack users of changes to your AWS account using CloudWatch Events

### Features 

Notifon currently has the following features:

- Send notifications to Slack when CloudWatch events happen