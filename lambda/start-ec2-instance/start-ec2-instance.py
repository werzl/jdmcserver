import os
import json
import boto3


def lambda_handler(event, context):
    region = os.environ['region']
    #region = "eu-west-2"

    instance_ids = [os.environ['instanceId']]
    #instance_ids = ['i-029f683986573a67e']
    
    ec2_resource = boto3.resource('ec2', region_name=region)

    try:
        ec2_resource.instances.filter(InstanceIds=instance_ids).start()
        return {
            'statusCode': 200,
            'body': json.dumps({'running': True}),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }
    except Exception as e:
        print('Failed to stop instance ' + instance_ids[0])
        print(e)


#lambda_handler("test", "test")