import aws_cdk as cdk
import aws_cdk.aws_sqs as sqs
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_lambda_event_sources as eventsources
import aws_cdk.aws_dynamodb as ddb
from constructs import Construct


# Build a Stack with SQS -> lambda -> DDB
# events from sqs are picked up by a lambda, which saves them in a DDB table
class Infra(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create the queue
        queue = sqs.Queue(
            self, "InfraStackQueue",
            visibility_timeout=cdk.Duration.seconds(300),
        )

        # create the lambda function
        fn = lambda_.Function(self, "InfraStackLambda",
                              runtime=lambda_.Runtime.PYTHON_3_8,
                              handler="handler.lambda_handler",
                              code=lambda_.Code.from_asset("monorepo_cdk")
                              )

        # set up the queue as an event source to the lambda
        fn.add_event_source(eventsources.SqsEventSource(queue))

        # create the Dynamo DB table and grant r/w permission tot he lambda function
        table = ddb.Table(self, "InfraStackDDB",
                                partition_key=ddb.Attribute(name="id", type=ddb.AttributeType.STRING))
        table.grant_read_write_data(fn)

        # the actual table name is not known until deployment, create a token and pass it as an env var to the lambda
        fn.add_environment("infra_ddb_table", table.table_name)
