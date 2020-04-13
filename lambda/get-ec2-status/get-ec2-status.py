import os
import json
import boto3

def lambda_handler(event, context):    
    region = os.environ['region']
    #region = "eu-west-2"

    instance_id = os.environ['instanceId']
    #instance_id = 'i-029f683986573a67e'

    ec2_resource = boto3.resource('ec2', region_name=region)

    instance = ec2_resource.Instance(instance_id)
    if instance.state['Name'] == 'running':
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'Running'}),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }
    elif instance.state['Name'] == 'stopped':
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'Stopped'}),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'Pending'}),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }


#print(lambda_handler("test", "test"))
