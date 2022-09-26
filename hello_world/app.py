import json
import boto3
import os


def lambda_handler(event, context):
    client = boto3.client('s3')
    try:
        response = client.get_object(Bucket='static.test.video', Key='robots.txt')
        content = response.get('Body').next().decode()
    except Exception as e:
        print(e)
        content = ''
    if hasattr(context, 'invoked_function_arn'):
        alias_function = context.invoked_function_arn.split(':')[-1]
        print(alias_function)
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'statusDescription': '200 OK',
        'headers': {
            'Set-cookie': 'cookies',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': content,
        }),
    }
