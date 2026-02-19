import boto3  # Import the AWS SDK for Python so we can interact with AWS services.

# Create an EC2 client.
# Even though we’re working with VPCs, VPCs are part of the EC2 service in AWS.
vpc_client = boto3.client('ec2')

# Call the EC2 API to retrieve information about all VPCs in the account/region.
# The result comes back as a dictionary containing metadata and a list of VPCs.
response = vpc_client.describe_vpcs()

# Extract the list of VPC dictionaries from the response.
# Each item in this list represents one VPC and contains many properties.
vpcs = response['Vpcs']

# Loop through each VPC in the list.
for vpc in vpcs:
    # Print the VPC ID (for example: vpc-0abc1234def567890)
    print(vpc['VpcId'])
