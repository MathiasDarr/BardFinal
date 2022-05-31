from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class DeploymentStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open('userdata.sh') as f:
            script = f.read()
        user_data = ec2.UserData.custom(script)
        vpc = ec2.Vpc.from_lookup(self, vpc_id='vpc-0be4b47e24b58c7e5', is_default=True, id="bard-vpc")

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
                                user_data=user_data,
                                machine_image=ec2.MachineImage.latest_amazon_linux(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                key_name='bard'
                            )

        # core.CfnOutput(self, 'bardip', value=instance.ins)
