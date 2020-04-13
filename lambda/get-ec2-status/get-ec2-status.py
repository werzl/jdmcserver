import os
import json
import boto3

def lambda_handler(event, context):
    instance_id = os.environ['instanceId']
    ec2_resource = boto3.resource('ec2', region_name='eu-west-2')
    # instance_id = 'test'

    instance = ec2_resource.Instance(instance_id)
    if instance.state['Name'] == 'running':
        return {
            'statusCode': 200,
            'body': json.dumps({'running': True}),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'running': False}),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }


#print(lambda_handler("test", "test"))
