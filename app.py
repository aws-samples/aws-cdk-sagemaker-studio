#!/usr/bin/env python3

from aws_cdk import core

from sagemakerStudioCDK.sagemaker_studio_stack import SagemakerStudioStack
import os
import boto3

sts_client = boto3.client("sts")
account_id = os.environ.get('CDK_DEFAULT_ACCOUNT', sts_client.get_caller_identity()["Account"])
region = os.environ.get('CDK_DEFAULT_REGION', 'eu-west-1')

app = core.App()
SagemakerStudioStack(app, "sagemakerStudioCDK", env={"account": account_id, 'region': region})

app.synth()
