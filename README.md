# Automation-in-AWS-EC2-using-Python-Scripts-and-Boto3-Library-
Scripts on various tasks on AWS EC2 environment

REQUIREMENTS:
- AWS account with admin priviledges
- Linux shell environment
- Python3 
- Python package manager, use pip to install the Boto3 library and the AWS CLI tool.

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

