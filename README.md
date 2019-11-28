# License Plate Text Recognition using AWS Textract/AWS Rekognition[Cloud]

## About
Powerful tool to recognise license plates of vehicles from a video and convert them to text data for storage/data analysis

Uses AWS Services such as Textract and Rekognition to efficiently extract text from the video


**Keywords:** AWS API, EC2 instance, Cloud, Textract, Rekognition, python, OpenCV, Ubuntu, boto3, numpy, License Plate Recognition, Alpr, Image analysis, Real life image text recognition 
## How it works?  

 - Extract frames from the video as images (OpenCV)
 - Pass the frames to [AWS Textract](https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html) or [AWS Rekognition](https://aws.amazon.com/rekognition) service to analyse and get detected text in the frames
 - Output detected text data to file/command prompt with timestamp

## Pre-Requisites

 - OpenCV with Python3
 - AWS Ubuntu Linux VM EC2 instance with SSH Access (Free Tier works for testing/limited use)

## Files in this repository


| Sl NO|FileName|Functionality  | Requirements|
|--|--|--|--|
| 1| [`VideoParserFPS.py`](https://github.com/yakshaG/aws-LicensePlateRecognition/blob/master/VideoParserFPS.py) | Parses a local video file into frames at a specified frame rate and displays the parsed frames | 1. OpenCV with Python (Python3 for uniformity across the project)<br> 2. `numpy` python module|
| 2| [`TextractLocal.py`](https://github.com/yakshaG/aws-LicensePlateRecognition/blob/master/TextractLocal.py)| Processes a local image file (frame) using AWS Textract API and returns the result | 1. AWS Ubuntu Linux EC2 Instance over SSH with `Textract` Security policies applied to IAM role of the instance <br> 2. `boto3` python module|
| 3| [`RekognitionLocal.py`](https://github.com/yakshaG/aws-LicensePlateRecognition/blob/master/RekognitionLocal.py)| Processes a local image file (frame) using AWS Rekognition API and returns the result. Claimed to produce better results than Textract on real life images. | 1. AWS Ubuntu Linux EC2 Instance over SSH with `Rekognition` Security policies applied to IAM role of the instance <br> 2. `boto3` python module|
| 4|[`TextractParserCumDetector.py`](https://github.com/yakshaG/aws-LicensePlateRecognition/blob/master/TextractParserCumDetector.py) | Processes a local video file at a specified frame rate using Textract API and returns the extracted results with timestamp | 1. OpenCV with Python (Python3 for uniformity across the project), <br> 2. AWS Ubuntu Linux EC2 Instance over SSH with `Textract` Security policies applied to IAM role of the instance <br> 3. `boto3` and `numpy` python modules|
| 5|[`RekognitionParserCumDetector.py`](https://github.com/yakshaG/aws-LicensePlateRecognition/blob/master/RekognitionParserCumDetector.py) | Processes a local video file at a specified frame rate using Rekognition API and returns the extracted results with timestamp. Claimed to produce better results than Textract on real life images. | 1. OpenCV with Python (Python3 for uniformity across the project), <br> 2. AWS Ubuntu Linux EC2 Instance over SSH with `Rekognition` Security policies applied to IAM role of the instance <br> 3. `boto3` and `numpy` python modules|

***Files above are not dependent on each other.***

 - Use `VideoParserFPS.py` to test parsing
 - Use `TextractLocal.py` and `RekognitionLocal.py` to test Text Detection on a frame
 - Use  `TextractParserCumDetector.py` and `RekognitionParserCumDetector.py` for combined full functionality

## Usage
Run the files in Ubuntu EC2 instance. Make sure to assign an IAM Role to the instance with Textract/Rekognition Policies attached. API calls to Textract/Rekognition will not work without these.
 - `python3 VideoParserFPS.py` 
 - `python3 TextractLocal.py`

and so on...
### Parameters to be set
 - Run the desired file from the same directory where `frame.jpg` or `video.mp4` is present. Frame name/Video Name hard coded
 - Set aws-region in files 2, 3, 4, 5

## Quick Guide to Install Requirements

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
## Additional

 - [x] Use `python3 TextractParserCumDetector.py >> DataDump.csv` to redirect output to csv file for further analysis
 - [ ] Post processing of data and cleaning to make it more practically useful

