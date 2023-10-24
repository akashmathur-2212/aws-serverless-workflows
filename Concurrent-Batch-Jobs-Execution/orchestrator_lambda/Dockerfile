FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy function code
COPY lambda_function.py .

RUN echo "Image Built"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["lambda_function.lambda_handler"]
