from aws_cdk import (
    Stack,
    aws_s3 as s3,
)
from constructs import Construct

class UdemyCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self,
            "JimFirstBucket",
            bucket_name="jim-first-bucket-101010",
            versioned=True,
            encryption=s3.BucketEncryption.KMS_MANAGED
        )
