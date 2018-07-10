########### Automation on AWS EC2 - Stopping Multiple Instances ###############
###  
###			Please follow the steps in README file to set up the environment
###
###
###  Create a JSON file with the Instance ID that needs to be terminated in the following format:
###  Please refer to aws_ec2_stopping_instances.json file uploaded.
###  
###{
###	"InstanceID":["i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX"]
###}
###

import boto3
import json

client = boto3.client('ec2')
ec2= boto3.resource('ec2')

#Read the JSON file
json_file = open("C:/AWS Scripts/aws_ec2_stopping_instances.json", "r")
data = json.load(json_file)

InstanceID =[]
InstanceID = data["InstanceID"]
for x in range(len(InstanceID)):
	instance = client.stop_instances(InstanceIds = [InstanceID[x]])
	
#List all the Instances
for instance in ec2.instances.all():
	print(instance.id, instance.state, instance.tags)
