from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_secretsmanager as secretsmanager,
    core
)
import os
import json

class SSHSecretsManagerStack(core.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        home = os.environ.get('HOME')

        with open(f'{home}/.ssh/bard.pem') as f:
            data = f.read()


        secretsmanager.Secret(self,"bard_ssh",generate_secret_string=secretsmanager.SecretStringGenerator(secret_string_template=json.dumps({'key':data}), generate_string_key="key"))

        #secretsmanager.Secret(self, "bards_ssh",)

        # # Templated secret
        # secrets = secretsmanager.Secret(self, "BardSsh",
        #                                         secret_name="bard_ssh",
        #                                 secr
        #
        #                             )

