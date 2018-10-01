import boto3

ec2 = boto3.client('ec2')

# Retrive all regions/endpoints that work with EC2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

# Regions[].{Name:RegionName}

# Retrive availibility Zones only for a region of the ec2 object
response = ec2.describe_availability_zones()
print('Availability Zones:', response['AvailabilityZones'])

