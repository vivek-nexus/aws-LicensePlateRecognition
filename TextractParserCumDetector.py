# Try TextractLocal.py to test Textract functionality on a single local image
# Use python3 TextractParserCumDetector.py >> DataDump.csv to redirect output of parser to csv file for further analysis

import numpy as np
import cv2 as cv
import time
import os
import datetime
import boto3

# specify your region where your AWS resources are located. Textract is available only in select regions
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

# Document for parsing in same directory as this file, every frame during parsing below, will overwrite this file
documentName = "frame.jpg"

fpsLimit = 0.5 # frames per second
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
       #  print("Image written, handing over to AWS textract:")

        ##################### AWS Textract AREA, PAID SERVICE BEYOND FREE TIER LIMITS!  ########################
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
                print (item["Text"] + "," + now.strftime("%Y %m %d %H %M %S")) # prints detected text with timestamp of detection in comma separated fashion, can be collected as a csv file
                # print ('\033[94m' +  item["Text"] + '\033[0m')
        print('\n')

        ################### END OF AWS AREA ####################################


        startTime = time.time() # reset time
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
