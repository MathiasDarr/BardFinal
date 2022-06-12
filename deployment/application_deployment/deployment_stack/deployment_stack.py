from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)

class DeploymentStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open('userdata.sh') as f:
            script = f.read()
        user_data = ec2.UserData.custom(script)
        vpc = ec2.Vpc.from_lookup(self, "VPC",
                                  # This imports the default VPC but you can also
                                  # specify a 'vpcName' or 'tags'.
                                  is_default=True
                                  )
        account = kwargs.get('env').account

        ecr_policy = iam.ManagedPolicy.from_managed_policy_arn(self, id='managed_ecr_policy', managed_policy_arn=f"arn:aws:iam::{account}:policy/ecr_full_access")

        ec2_role = iam.Role(
            self,
            "bard_ec2_role",
            role_name="bard_role",
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[ecr_policy]
        )
        #
        bard_sg = ec2.SecurityGroup(
            self,
            id='bard-sg',
            vpc=vpc,
            description='Security Group',
            allow_all_outbound=True
        )

        bard_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port(
                protocol=ec2.Protocol.TCP, from_port=22, to_port=22, string_representation="not sure what this is"
            )
        )

        instance = ec2.Instance(self,
                                id="dakobed-ec2",
                                vpc=vpc,
                                security_group=bard_sg,
                                instance_type=ec2.InstanceType.of(
                                    ec2.InstanceClass.BURSTABLE3,
                                    ec2.InstanceSize.MICRO
                                ),
                                role=ec2_role,
                                user_data=user_data,
                                machine_image=ec2.MachineImage.latest_amazon_linux(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                key_name='bard'
                            )

        core.CfnOutput(self, 'bardip', value=instance.instance_public_ip)
