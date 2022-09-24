import json

# import requests
import os


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    path = os.environ.get('PATH')
    message = 'This is a message {}'.format(path)
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'statusDescription': '200 OK',
        'headers': {
            'Set-cookie': 'cookies',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': message,
        }),
    }
