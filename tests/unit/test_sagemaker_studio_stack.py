import json
import pytest

from aws_cdk import core
from sagemakerStudioCDK.sagemaker_studio_stack import SagemakerStudioStack


def get_template():
    app = core.App()
    SagemakerStudioStack(app, "sagemakerStudioCDK")
    return json.dumps(app.synth().get_stack("sagemakerStudioCDK").template)


def test_sagemaker_domain_created():
    assert("AWS::SageMaker::Domain" in get_template())

