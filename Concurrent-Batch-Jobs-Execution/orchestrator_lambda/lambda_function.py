import numpy as np
import boto3
import awswrangler as wr

def lambda_handler(event, context):
    
    # Get the file details that has been PUT into the designated bucket
    BUCKET = event['Records'][0]['s3']['bucket']['name'] 
    KEY = event['Records'][0]['s3']['object']['key'] 
    
    print(BUCKET, KEY)
    config_file_path = f"s3://{BUCKET}/path-to-config-file/{KEY}"
         
    try:
        # read input files files
        config = wr.s3.read_csv(path=config_file_path)
        
    except Exception as e:
        print(f"An error occurred in reading the files: {e}")
        
    for idx in np.arange(config.shape[0]):
        row = config.iloc[idx]
    
        country = str(row["country"])
        column_1= str(row["column_1"])
        column_2= str(row["column_2"])
        column_3 = str(row["column_3"])
        
        print("Initialize the Batch client")
        # Initialize the AWS Batch client
        batch_client = boto3.client('batch')
        
        # Specify the job definition, job name, and job queue
        job_definition = 'job_definition'
        job_name = country
        job_queue = 'job-queue'

        try:
            print(f"Running {country} on batch")
            # Submit the job
            response = batch_client.submit_job(
                jobName=job_name,
                jobQueue=job_queue,
                jobDefinition=job_definition,
                containerOverrides= {
                    "environment": [
                        {
                            "name": "country",
                            "value": country
                        },
                        {
                            "name": "column_1",
                            "value": column_1
                        },
                        {
                            "name": "column_2",
                            "value": column_2
                        },
                        {
                            "name": "column_3",
                            "value": column_3
                        },
                    ]
                }
            )

            # Get the jobId from the response
            job_id = response['jobId']
            print(f'Batch job for {country} submitted successfully with job ID {job_id}')
        
        except Exception as e:
            print(f'Error submitting the batch job for {country}: {str(e)}')

    return {
        'statusCode': 200,
        'body': 'Batch jobs submitted successfully'
    }
