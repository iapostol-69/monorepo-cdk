import aws_cdk as core
import aws_cdk.assertions as assertions

from monorepo_cdk.monorepo_cdk_stack import MonorepoCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in monorepo_cdk/monorepo_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MonorepoCdkStack(app, "monorepo-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
