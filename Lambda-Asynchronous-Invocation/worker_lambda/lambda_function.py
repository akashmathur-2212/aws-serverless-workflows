import json
import pandas as pd
import numpy as np
import awswrangler as wr

def lambda_handler(event, context):
    
    # The event parameter contains the payload you provided when invoking this Lambda function
    payload = json.loads(event['Payload'])
    
    # Get the input details from event to instantiate the class
    country = payload["country"]
    column_1 = payload["column_1"]
    column_2 = payload["column_2"]
    
    """
    ENTER YOUR CODE HERE OR IMPORT A PYTHON MODULE
    
    """"
        
    print("Saving the results to S3.")
    wr.s3.to_csv(df=df, 
                 path=f"s3://saved-path.csv", 
                 index=False)
    print(f"{country} Completed.")
    
    return {
        "statusCode": 200,
        "body": json.dumps(f"{country} Completed.")
    }