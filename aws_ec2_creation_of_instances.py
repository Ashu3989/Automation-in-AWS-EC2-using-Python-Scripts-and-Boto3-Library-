##################################################################################
########### Automation on AWS EC2 - Creation of Multiple Instances ###############
###  
###			Please follow the steps in README file to set up the environment
###
###
###  Create a JSON file with the specification of the requirement in the following format:
###  Note: Here number of instances is 2, for more instances, update the "images" Collection.
###
###  
###		{
###		"VM":
###			{
###			"MinCount" :1,
###			"MaxCount":1,
###			"no_of_instances" : 2,
###			"InstanceType":"t2.micro",
###			"keyname":"Testing_VM",
###			"Images" : 
###					[
###						{
###						"ImageId" : "ami-3703414f",
###						"name": "Windows_Staging",
###						"IPAddress": 10.0.0.1,
###						"SecurityGroups": "SG_name"
###						},
###						{
###						"ImageId" : "ami-37023454f",
###						"name": "Linux_Prod",
###						"IPAddress": 10.0.0.2,
###						"SecurityGroup": "SG2_name"
###						}
###					
###					]
###						
###			}
###		}

import boto3
import json

#Read the JSON file 
json_file = open("C:/AWS Scripts/Data.json", "r")
data = json.load(json_file)

ec2 = boto3.resource('ec2')

#Accessing data from JSON
Images = data["VM"]["Images"]
number = data["VM"]["no_of_instances"]

# Attributes of instances
instance = []
minCount=data["VM"]["MinCount"]
maxCount=data["VM"]["MaxCount"]
instanceType=data["VM"]["InstanceType"]
keyName=data["VM"]["keyname"]

#Creation of instances for each  requirement described in JSON file
for i in Images:
	tag_purpose_test = {"Key": "Name", "Value": i["name"]}
	instance = ec2.create_instances(
		ImageId=i["ImageId"],
		MinCount=minCount,
		MaxCount=maxCount,
		InstanceType=instanceType,
		KeyName=keyName,
		TagSpecifications=[{'ResourceType': 'instance','Tags': [tag_purpose_test]}])

print("Instances is booting please wait.....")

time.sleep(5)


for instance in ec2.instances.all():
	print(instance.id, instance.state, instance.tags)
	
