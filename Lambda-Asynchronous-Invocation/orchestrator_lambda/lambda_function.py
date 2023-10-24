import json
import pandas as pd
import numpy as np
import boto3
import awswrangler as wr

def lambda_handler(event, context):
    
    # Get the file details that has been PUT into the designated bucket
    BUCKET = event['Records'][0]['s3']['bucket']['name']
    KEY = event['Records'][0]['s3']['object']['key']
    
    print(BUCKET, KEY)
    config_file_path = f"s3://{BUCKET}/AWS_workflow/techvio_lambda_trigger/config_upload/{KEY}"
         
    try:
        # read input files files
        config = wr.s3.read_csv(path=config_file_path)
        
    except Exception as e:
        print(f"An error occurred in reading the files: {e}")
        
    print("Creating a Lambda client")
    # Create an AWS Lambda client
    lambda_client = boto3.client('lambda')
     
    for idx in np.arange(config.shape[0]):
        row = config.iloc[idx]
    
        country = str(row["country"])
        print(f"Running: {country}")
        
        vio_start_year = int(row["vio_start_year"])
        vio_end_year = int(row["vio_end_year"])
        
        # Customize the payload with the necessary data
        payload = {
            "country": country,
            "vio_start_year": vio_start_year,
            "vio_end_year": vio_end_year
            }
        
        # Invoke an AWS Lambda function for each row concurrently
        lambda_client.invoke(
            FunctionName='arn:aws:lambda:us-east-1:477191530357:function:techvio_worker_lambda',
            InvocationType='Event',  # Asynchronous invocation
            Payload=json.dumps(payload)
        )
        print(f"Lambda invoked for {country}")
        
    return {
        "statusCode": 200,
        "body": json.dumps("Process completed!")
    }