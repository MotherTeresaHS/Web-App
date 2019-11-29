import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    
    #boto3.setup_default_session(region_name='us-east-1')
    #identity = boto3.client('cognito-identity', region_name='us-east-1')
    
    #account_id='XXXXXXXXXXXXXXX'
    #identity_pool_id='us-east-1_NEm4KpQy1'
    #api_prefix='ZZZZZZZZZ'
    
    #response = identity.get_id(AccountId=account_id, IdentityPoolId=identity_pool_id)
    #identity_id = response['IdentityId']
    #print ("Identity ID: %s"%identity_id)
    
    # The output from a Lambda proxy integration must be 
    # in the following JSON object. The 'headers' property 
    # is for custom response headers in addition to standard 
    # ones. The 'body' property  must be a JSON string. For 
    # base64-encoded payload, you must also set the 'isBase64Encoded'
    # property to 'true'.
    
    cognito = boto3.client('cognito-identity')
    response = cognito.get_credentials_for_identity(IdentityId="cognito-idp.us-east-1.amazonaws.com/NEm4KpQy1")
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
