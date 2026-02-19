import boto3  # Import the AWS SDK for Python. This lets Python talk to AWS services.

# Create an S3 client object.
# boto3 automatically looks for AWS credentials in environment variables,
# config files, or IAM roles if running inside AWS.
s3 = boto3.client('s3')

# Call the AWS S3 API to get a list of all S3 buckets in the account.
# The result is returned as a Python dictionary containing metadata.
response = s3.list_buckets()

# From the response dictionary, grab the value associated with the "Buckets" key.
# This is a list of bucket objects (each bucket is represented as a dictionary).
buckets = response["Buckets"]

# Loop through each bucket in the list.
for bucket in buckets:
    # Each bucket dictionary contains fields like "Name" and "CreationDate".
    # Print only the bucket's name.
    print(bucket["Name"])
