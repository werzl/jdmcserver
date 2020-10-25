import os
import json
import boto3

def lambda_handler(event, context):
    region = os.environ['region']
    #region = "eu-west-2"
    
    instance_ids = [os.environ['instanceId']]
    #instance_ids = ['i-029f683986573a67e']

    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.describe_instances(InstanceIds=[instance_ids])
    instance_details = {}
    instance_details['launchTime'] = response['Reservations'][0]['Instances'][0]['LaunchTime'].strftime('%Y-%m-%dT%H:%M:%SZ')
    instance_details['availabilityZone'] = response['Reservations'][0]['Instances'][0]['Placement']['AvailabilityZone']
    instance_details['publicDnsName'] = response['Reservations'][0]['Instances'][0]['PublicDnsName']
    instance_details['publicIpAddress'] = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    instance_details['instanceState'] = response['Reservations'][0]['Instances'][0]['State']['Name']
    
    return {
            'statusCode': 200,
            'body': json.dumps(instance_details),
            'headers': {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            }
        }

#print(lambda_handler("",""))