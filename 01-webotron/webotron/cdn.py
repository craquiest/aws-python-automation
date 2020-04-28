# -*- coding: utf-8 -*-

"""Classes for Cloud Front Distributions."""

import uuid


class DistributionManager:
    """Manage CloudFront distributions."""

    def __init__(self, session):
        """Create a DistributionManager."""
        self.session = session
        self.client = self.session.client('cloudfront')

    def find_matching_dist(self, domain_name):
        """Find a dist matching domain_name."""
        paginator = self.client.get_paginator('list_distributions')
        for page in paginator.paginate():
            # print(page)
            for dist in page['DistributionList'].get('Items', []):
                for alias in dist['Aliases']['Items']:
                    if alias == domain_name:
                        return dist

        return None

    def create_dist(self, domain_name, cert, website_url):
        """Create a dist for domain_name using cert."""
        #! Extra param 'website_url' to use as cdn origin
        origin_id = 'S3-' + domain_name

        #! Lamine:  change Origins domain name to website_naked_url  i.o. bucket_domain_name
        #! 'CustomOriginConfig' needs to be set, 'S3OriginConfig' no longer needed
        bucket_domain_name = '{}.s3.amazonaws.com'.format(domain_name) # originally used in 'Origins'
        print("CDN origin to be set to" + website_url)

        #TODO: change Aliases to include www.domain_name and *.domain_name. Qty set to 3 from 1

        result = self.client.create_distribution(
            DistributionConfig={
                'CallerReference': str(uuid.uuid4()),
                'Aliases': {
                    'Quantity': 1,
                    'Items': [domain_name]
                },
                'DefaultRootObject': 'index.html',
                'Comment': 'Created by webotron',
                'Enabled': True,
                'Origins': {
                    'Quantity': 1,
                    'Items': [{
                        'Id': origin_id,
                        'DomainName':
                        website_url,
                        # 'S3OriginConfig': {
                        #     'OriginAccessIdentity': ''
                        # },
                        'CustomOriginConfig': {
                            'HTTPPort': 80,
                            'HTTPSPort': 443,
                            'OriginProtocolPolicy': 'http-only',
                            # 'OriginSslProtocols': {
                            #     'Quantity': 1,
                            #     'Items': [
                            #         'TLSv1.1'
                            #     ]
                            # }#,
                            # 'OriginReadTimeout': 123,
                            # 'OriginKeepaliveTimeout': 123
                        }
                    }]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': origin_id,
                    'ViewerProtocolPolicy': 'redirect-to-https',
                    'TrustedSigners': {
                        'Quantity': 0,
                        'Enabled': False
                    },
                    'ForwardedValues': {
                        'Cookies': {'Forward': 'all'},
                        'Headers': {'Quantity': 0},
                        'QueryString': False,
                        'QueryStringCacheKeys': {'Quantity': 0}
                    },
                    'DefaultTTL': 60,#86400,
                    'MinTTL': 0 #3600
                },
                'ViewerCertificate': {
                    'ACMCertificateArn': cert['CertificateArn'],
                    'SSLSupportMethod': 'sni-only',
                    'MinimumProtocolVersion': 'TLSv1.1_2016'
                }
            }
        )

        return result['Distribution']

    def await_deploy(self, dist):
        """Wait for dist to be deployed."""
        waiter = self.client.get_waiter('distribution_deployed')
        waiter.wait(Id=dist['Id'], WaiterConfig={
            'Delay': 30,
            'MaxAttempts': 50
        })
