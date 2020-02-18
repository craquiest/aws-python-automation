#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Webotron: Deploy websites with aws,as per a.cloud.guru course AWS python Automation.

Webotron automates the proceess of deployiing static websites on AWS.
- Configure AWS S3 buckets
  - Create them
  - Set them up for static website hosting
  - Deploy local files to them
- Configure DNS with AWS Route 53
- Configure a Content Delivery Network and SSL with AWS Cloudfront
"""
from pathlib import Path
import mimetypes

import boto3
from botocore.exceptions import ClientError
import click
# import sys

session = boto3.Session(profile_name='craquiest')
s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploys websites to AWS."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an s3 bucket."""
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = None
    try:
        s3_bucket = s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={
                'LocationConstraint': session.region_name}
        )
    except ClientError as error:
        if error.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = s3.Bucket(bucket)
        else:
            raise error

    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[{
      "Sid":"PublicReadGetObject",
      "Effect":"Allow",
      "Principal": "*",
          "Action":["s3:GetObject"],
          "Resource":["arn:aws:s3:::%s/*"
          ]
        }
      ]
    }
    """ % s3_bucket.name
    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)

    s3_bucket.Website().put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },
        'IndexDocument': {
            'Suffix': 'index.html'
        }
    })

    return


def upload_file(s3_bucket, path, key):
    """Upload file to S3 bucket. Ppath and key represent directory and filename."""
    content_type = mimetypes.guess_type(key)[0] or 'text/plain'
    s3_bucket.upload_file(
        path, key,
        ExtraArgs={'ContentType': content_type}  # 'test/html'
    )


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    s3_bucket = s3.Bucket(bucket)
    # * get the root path, as absolute path (resolve())
    # * and platform independent (expanduser())
    root = Path(pathname).expanduser().resolve()

    def handle_directory(target):
        for p in target.iterdir():
            if p.is_dir():
                # * Call recursively till you get files
                handle_directory(p)
            if p.is_file():
                upload_file(s3_bucket, str(p), str(p.relative_to(root)))

    handle_directory(root)


if __name__ == '__main__':
    # print(sys.argv)
    cli()
