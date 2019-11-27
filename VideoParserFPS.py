import numpy as np
import cv2 as cv
import time

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
        cv.imshow('frame', frame)
        print("Image written")
        cv.imwrite("frame.jpg", frame) # frame will be written to disk
        startTime = time.time() # reset time
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
