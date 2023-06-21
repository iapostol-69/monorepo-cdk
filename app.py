#!/usr/bin/env python3
import os
import aws_cdk as cdk
from monorepo_cdk.monorepo_cdk_stack import MonorepoCdkStack


app = cdk.App()
pipeline = MonorepoCdkStack(app, "MonorepoCdkStack",
                            env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                                                region=os.getenv('CDK_DEFAULT_REGION')))

app.synth()