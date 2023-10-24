FROM public.ecr.aws/amazonlinux/amazonlinux:2023

WORKDIR /app

# Install software
RUN yum update -y && \
    yum install -y python39 && \
    python3 -m ensurepip --upgrade && \
    python3 -m pip install --upgrade setuptools

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install -r /app/requirements.txt

COPY . .

RUN echo "Image Built"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile) #"python3", "-u"
CMD ["python3", "worker_function.py"]