import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from monorepo_cdk.infra_stage import InfraStage


class MonorepoCdkStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        synth_step = ShellStep("Synth",
                               input=CodePipelineSource.git_hub(repo_string="iapostol-69/monorepo-cdk", branch="master"),
                               commands=["npm install -g aws-cdk",
                                         "python -m pip install -r requirements.txt",
                                         "cdk synth"])

        pipeline = CodePipeline(self,
                                "Pipeline",
                                pipeline_name="MonoRepoPipeline",
                                synth=synth_step)

        pipeline.add_stage(InfraStage(self, "InfraStage"))


