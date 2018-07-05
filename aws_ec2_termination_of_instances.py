########### Automation on AWS EC2 - Termination of Multiple Instances ###############
###  
###			Please follow the steps in README file to set up the environment
###
###
###  Create a JSON file with the Instance ID that needs to be terminated in the following format:
###  
###Termination_Data.json file:
###{
###	"InstanceID":["i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX" ,"i-XXXXXXXX"]
###}
###



import boto3
import json

ec2 = boto3.resource('ec2')

#Read the JSON file 
json_file = open("C:/AWS Scripts/Termination_Data.json", "r")
data = json.load(json_file)

InstanceID =[]
InstanceID = data["InstanceID"]
for x in range(len(InstanceID)):
	instance = ec2.Instance(InstanceID[x])
	response = instance.terminate()
	
#List all the Instances
for instance in ec2.instances.all():
	print(instance.id, instance.state, instance.tags)
	




