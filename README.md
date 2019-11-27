# License Plate Text Recognition using AWS Textract/AWS Rekognition[Cloud]

This repository contains files of a project used to **recognize license plates from real life footage of vehicles**.

## Project Workflow  

 - Parse a video file to extract frames with custom FPS (OpenCV)
 - Pass the frame to [AWS Textract](https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html) or [AWS Rekognition](https://aws.amazon.com/rekognition/?nc=sn&loc=0) service to analyse and return results
 - All processing performed on the cloud on AWS EC2 VM instance

## Pre-Requisites

 - OpenCV with Python3
 - AWS Ubuntu Linux VM EC2 instance with SSH Access (Free Tier works for testing/limited use)

## Files in this repository


| Sl NO|FileName|Functionality  | Requirements|
|--|--|--|--|
| 1| `VideoParserFPS.py` | Parses a local video file into frames at a specified frame rate and displays the parsed frames | 1. OpenCV with Python (Python3 for uniformity across the project)<br> 2. `numpy` python module|
| 2| `TextractLocal.py`| Processes a local image file (frame) using AWS Textract API and returns the result | 1. AWS Ubuntu Linux EC2 Instance over SSH with `Textract` Security policies applied to IAM role of the instance <br> 2. `boto3` python module|
| 3| `RekognitionLocal.py`| Processes a local image file (frame) using AWS Rekognition API and returns the result. Claimed to produce better results than Textract on real life images | 1. AWS Ubuntu Linux EC2 Instance over SSH with `Rekognition` Security policies applied to IAM role of the instance <br> 2. `boto3` python module|
| 4|`TextractParserCumDetector.py` | Processes a local video file at a specified frame rate using Textract API and returns the extracted results with timestamp | 1. OpenCV with Python (Python3 for uniformity across the project), <br> 2. AWS Ubuntu Linux EC2 Instance over SSH with `Textract` Security policies applied to IAM role of the instance <br> 3. `boto3` and `numpy` python modules|
| 5|`RekognitionParserCumDetector.py` | Processes a local video file at a specified frame rate using Rekognition API and returns the extracted results with timestamp | 1. OpenCV with Python (Python3 for uniformity across the project), <br> 2. AWS Ubuntu Linux EC2 Instance over SSH with `Rekognition` Security policies applied to IAM role of the instance <br> 3. `boto3` and `numpy` python modules|

***Files above are not dependent each other.***

 - Use `VideoParserFPS.py` to test parsing
 - Use `TextractLocal.py` and `RekognitionLocal.py` to test Text Detection on a frame
 - Use  `TextractParserCumDetector.py` and `RekognitionParserCumDetector.py` for combined full functionality

## Usage
Run the files in Ubuntu EC2 instance. Make sure to assign an IAM Role to the instance with Textract/Rekognition Policies attached. API calls to Textract/Rekognition will not work without these.
 - `python3 VideoParserFPS.py` 
 - `python3 TextractLocal.py`

### Parameters to be set
 - Run the desired file from the same directory where `frame.jpg` or `video.mp4` is present. Frame name/Video Name hard coded
 - Set aws-region in files 2, 3, 4, 5

## Quick Guide to install Requirements

 ### OpenCV
 ```
sudo apt update
sudo apt install python3-opencv
```
You may want to [compile OpenCV from source](https://docs.opencv.org/master/d2/de6/tutorial_py_setup_in_ubuntu.html) if above method doesn't work.

### Python3 modules
```
sudo apt update
sudo apt install python3-pip

sudo pip3 install numpy
sudo pip3 install boto3
```

