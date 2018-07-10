##################################################################################################
########### Automation on AWS EC2 - Create and Attach volume to Multiple Instances ###############
###  
###			Please follow the steps in README file to set up the environment
###
###
###  Create a JSON file with the specification of the requirement in the following format:
###  Please refer to aws_ec2_attach_volumes_instances.json file uploaded.
###  
###  Note: Here number of volume created are 2, for more instances, update the "Volumes" Collection.
###        The Device Name terminology are different for different OS,
### 	   therefore, please lookup for available device names in AWS documentation. Only those names are accepted.
###		   	
###  
###		{
###		"VM":
###			{
###			"Volumes" : 
###					[
###						{
###						"InstanceID" : "i-XXXXXXXXXXX",
###						"Size": 5,
###						"Device_Name": "xvdc"
###						},
###						{
###						"InstanceID" : "i-XXXXXXXXXXX",
###						"Size": 5,
###						"Device_Name": "xvdb"
###						}
###					
###					]
###						
###			}
###		}

import boto3
import json
import time

ec2 = boto3.resource('ec2')
#ec2= boto3.client('ec2')

#Read the JSON file
json_file = open("C:/AWS Scripts/aws_ec2_attach_volumes_instances.json", "r")
data = json.load(json_file)

#Accessing data from JSON
Volumes = data["VM"]["Volumes"]
number = data["VM"]["no_of_instance"]

lun = []


# lun=1
# print(lun)
for volume in Volumes:
	lun= ec2.create_volume(Size=volume["Size"],AvailabilityZone="us-west-2a")
	#count= count+1
	time.sleep(10)
	response = lun.attach_to_instance(
		Device=volume["Device_Name"],
		InstanceId=volume["InstanceID"])
		
	print(lun)
	print("Luns attached to respective instance ID" )



