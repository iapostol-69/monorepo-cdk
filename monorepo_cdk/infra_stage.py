import aws_cdk as cdk
from constructs import Construct
from monorepo_cdk.infra import Infra


class InfraStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        infra_stack = Infra(self, "InfraStack")