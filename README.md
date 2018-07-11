# Automation-in-AWS-EC2-using-Python-Scripts-and-Boto3-Library-
Scripts on various tasks on AWS EC2 environment

REQUIREMENTS:
- AWS account with admin priviledges
- Linux shell environment
- Python3 
- Python package manager, use pip to install the Boto3 library and the AWS CLI tool.

Run the below commands in command prompt to check:
- For Python Version type "python -V". The version should be 2.6 or greater.
- For pip version type "pip -V". the version should be 9.0.1 or newer.

GETTING CONFIGURED:
- Using the pip command, install the AWS CLI and Boto3:

  C:\>pip install awscli boto3 -U --ignore-installed six
  
- IAM USER : Give the user permissions to interact with specific services, and get credentials to identify that user.

- Configure the scripting environment with the AWS CLI tool.

  C:\>aws configure
  
  C:\>AWS Access Key ID [None]: XXXXXXXXXXXXXXXXX
  
  C:\>AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  
  C:\>Default region name [None]: us-west-2
  
  C:\>Default output format [None]: text
  
  ****The above steps configures your environment****

