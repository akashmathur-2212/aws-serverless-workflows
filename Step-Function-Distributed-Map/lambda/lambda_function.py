# Lambda Function: post-pocessing Function
import json
import re

def lambda_handler(event, context):
    # Assuming event contains the row data
    row_data = event['column_name'] 
    
    # Perform your post-processing operations on row_data
    cleaned_text = re.sub(r'[^A-Za-z\s]', '', row_data)

    # Remove extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    processed_result = f"Processed data: {cleaned_text}"

    return {
        'statusCode': 200,
        'body': json.dumps(processed_result)
    }
