import os
import json
import boto3


def lambda_handler(event, context):
    region = os.environ['region']
    instance_ids = [os.environ['instanceId']]
    ec2_resource = boto3.resource('ec2', region_name=region)
    #instance_ids = ['i-029f683986573a67e']

    try:
        ec2_resource.instances.filter(InstanceIds=instance_ids).stop()
        return {
            'statusCode': 200
        }
    except Exception as e:
        print('Failed to stop instance ' + instance_ids[0])
        print(e)


#lambda_handler("test", "test")