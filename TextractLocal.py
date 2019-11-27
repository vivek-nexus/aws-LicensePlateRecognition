# Use this program to test Textract functionality on a single local image frame.jpg

import boto3
import os
import datetime

# specify your region where your AWS resources are located. Textract is available only in select regions
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

# Document for parsing in same directory as this file
documentName = "frame.jpg"

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.detect_document_text(Document={'Bytes': imageBytes})

# print(response)

# Print detected text
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        now = datetime.datetime.now()
        print (item["Text"] + "   " + now.strftime("%Y-%m-%d %H:%M:%S")) # prints extracted text with time stamp of extraction
        # print ('\033[94m' +  item["Text"] + '\033[0m')
