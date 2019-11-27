# Use this program to test Rekognition functionality on a single local image frame.jpg

import boto3
import os
import datetime

# specify your region where your AWS resources are located. Rekognition is available only in select regions
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

# Document for parsing in same directory as this file
documentName = "frame.jpg"

# Read document content
with open(documentName, 'rb') as document:
    imageBytes = bytearray(document.read())

# Amazon Rekognition client
client=boto3.client('rekognition')

# Call Amazon Rekognition
response=client.detect_text(Image={'Bytes': imageBytes})
textDetections=response['TextDetections']
# print(response)

# Print detected text
print ('Detected text\n----------')
for text in textDetections:
        print ('Detected text:' + text['DetectedText']) #prints Detected text
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%") # prints confidence level
