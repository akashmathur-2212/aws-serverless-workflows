import json
import boto3

# grab environment variables
ENDPOINT_NAME = 'llm-endpoint-name'    
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Accept='application/json',
                                       Body=event['body'])

    response_payload = response['Body'].read().decode('utf-8')
    result = json.loads(response_payload)
    
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
 
