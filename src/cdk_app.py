from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_ec2 as ec2,
)

class MyInsecureStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, "UnencryptedBucket", bucket_name="test-unencrypted-bucket")
        
        ec2.SecurityGroup(self, "OpenSecurityGroup", vpc=ec2.Vpc(self, "TestVpc"),
                          allow_all_outbound=True, 
                          security_group_name="open-security-group")
