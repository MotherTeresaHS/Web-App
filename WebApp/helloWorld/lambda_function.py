from __future__ import print_function
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
import uuid


def lambda_handler(event, context):
    # this lambda function returns “Hello, World!” in JSON
    print(event)

    response = {
    "statusCode": 200,
    "headers": {},
    "body": json.dumps({
        "message": "Hello, World!"
        })
    }
    
    return response
