import json
import boto3

def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2', region_name='eu-west-2')

    instance = ec2_resource.Instance('i-029f683986573a67e')
    if instance.state['Name'] == 'running':
        return {
            'statusCode': 200,
            'body': json.dumps({'running': True})
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps({'running': False})
        }    


#print(lambda_handler("test", "test"))
