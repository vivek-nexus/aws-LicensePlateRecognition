#Try RekognitionLocal.py to test Textract functionality on a single local image
# Use python3 REKOParserCumDetector.py >> DataDump.csv to redirect output of parser to csv file for further analysis

import numpy as np
import cv2 as cv
import time
import os
import datetime
import boto3

# specify your region where your AWS resources are located. Rekognition is available only in select regions
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

# Document for parsing in same directory as this file, every frame during parsing below, will overwrite this file
documentName = "frame.jpg"

fpsLimit = 0.50 # frames per second
startTime = time.time()

# Video file to be in same directory as this file
cap = cv.VideoCapture('video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    nowTime = time.time()
    if (nowTime - startTime) > fpsLimit:
        # cv.imshow('frame', frame)
        cv.imwrite("frame.jpg", frame)
        # print("Image written, handing over to AWS textract:")

        ##################### AWS Textract AREA, PAID SERVICE BEYOND FREE TIER LIMITS!  ########################
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
        # print ('Detected text\n----------')
        for text in textDetections:
                now = datetime.datetime.now()
                print (text['DetectedText']+','+ now.strftime("%Y %m %d %H %M %S")) # prints detected text with timestamp of detection in comma separated fashion, can be collected as a csv file
                # print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('\n')

        ################### END OF AWS AREA ####################################


        startTime = time.time() # reset time
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
