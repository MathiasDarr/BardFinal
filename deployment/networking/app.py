#!/usr/bin/env python3
import os
from aws_cdk import(
    core
)

from stacks.ssh_secrets_manger_stack import SSHSecretsManagerStack

account = os.getenv("AWS_ACCOUNT")
region = "us-west-2"
env = core.Environment()
if account and region:
    env = core.Environment(account=account, region=region)

app = core.App()
SSHSecretsManagerStack(app,
                "BardSecretStack",
                env=env
                )

app.synth()
