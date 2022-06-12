#!/usr/bin/env python3
import os

from aws_cdk import core
from deployment_stack.deployment_stack import DeploymentStack

account = os.getenv("AWS_ACCOUNT")
region = "us-west-2"
env = core.Environment()
if account and region:
    env = core.Environment(account=account, region=region)


app = core.App()
DeploymentStack(app,
                "DakobedBardStack",
                env=env

                )

app.synth()
