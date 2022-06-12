#!/usr/bin/env python3

import aws_cdk as cdk

from ecr_repositories.ecr_repositories_stack import EcrRepositoriesStack


app = cdk.App()
EcrRepositoriesStack(app, "ecr-repositories")

app.synth()
