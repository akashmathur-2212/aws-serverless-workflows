import json
import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri


def get_sagemaker_config():
    
    # configure sagemaker execution role
    role = sagemaker.get_execution_role()
    
    # configure sagemaker instance details
    instance_type = "ml.g5.2xlarge"
    number_of_gpu = 1
    health_check_timeout = 300
    
    # configure HF details
    config = {
    'HF_MODEL_ID': "/opt/ml/model", # path to where sagemaker stores the model
    'SM_NUM_GPUS': json.dumps(number_of_gpu), # Number of GPU
    'MAX_INPUT_LENGTH': json.dumps(3072),  # Max input length
    'MAX_TOTAL_TOKENS': json.dumps(4096),  # Max length of the generated text
    'MAX_BATCH_TOTAL_TOKENS': json.dumps(8192),  # Limits the number of tokens that can be processed in parallel during the generation
    }
    
    return role, instance_type, health_check_timeout, config

def lambda_handler(event, context):
     
     #Get the file details that has been PUT into the designated bucket
     # BUCKET = event['Records'][0]['s3']['bucket']['name']
     # KEY = event['Records'][0]['s3']['object']['key']
     
     llm_model_path = f"s3://model-path/model.tar.gz"
     
     # retrieve the Docker image URI for the HF LLM DLC
     llm_image = get_huggingface_llm_image_uri(
          "huggingface",
          version="0.9.3"
     )
     
     # log the docker image URI
     print(f"llm image uri: {llm_image}")
     
     # get sagemaker config
     role, instance_type, health_check_timeout, config = get_sagemaker_config()
     
     # create HuggingFaceModel with the image uri and provided params
     llm_model = HuggingFaceModel(
     model_data = llm_model_path,
     role = role,
     image_uri = llm_image,
     env = config)
          
     try:
          # Deploy model to the endpoint
          llm = llm_model.deploy(
               initial_instance_count=1,
               instance_type=instance_type,
               endpoint_name="llm_endpoint",
               container_startup_health_check_timeout=health_check_timeout
          )

     except Exception as e:
          print("Error creating an endpoint:", str(e))