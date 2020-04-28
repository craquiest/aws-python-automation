from setuptools import setup

setup(
    name='webotron-82',
    version='0.2',
    author='Lamine Gaye via Robin Norwood',
    author_email='laminegaye@me.com',
    description='Webotron 82 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/craquiest/aws-python-automation/tree/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
