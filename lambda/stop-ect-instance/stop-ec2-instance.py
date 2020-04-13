import os
import json
import boto3


def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2', region_name='eu-west-2')
    instance_ids = [os.environ['instanceId']]
    #instance_ids = ['i-029f683986573a67e']

    try:
        ec2_resource.instances.filter(InstanceIds=instance_ids).stop()
        return {
            'statusCode': 200
        }
    except:
        print('Failed to stop instance ' + instance_ids[0])


#lambda_handler("test", "test")