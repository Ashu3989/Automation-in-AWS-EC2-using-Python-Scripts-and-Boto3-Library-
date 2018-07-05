# Automation-in-AWS-EC2-using-Python-Scripts-and-Boto3-Library-
Scripts on various Tasks on AWS EC2 environment

REQUIREMENTS:
- AWS account with admin priviledges
- Access to a Linux shell environment with an active internet connection.
- Python installed 
- Python package manager installed, We’ll use pip to install the Boto3 library and the AWS CLI tool.

GETTING CONFIGURED:
- Using the pip command, install the AWS CLI and Boto3:

  pip install awscli boto3 -U --ignore-installed six
  
- IAM USER : Give the user permissions to interact with specific services, and get credentials to identify that user.

- Configure the scripting environment with the AWS CLI tool.

  aws configure
  
  AWS Access Key ID [None]: XXXXXXXXXXXXXXXXX
  
  AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  
  Default region name [None]: us-west-2
  
  Default output format [None]: text
  
  ****The above steps configures your environment****

