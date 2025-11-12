# security-zone-tracker

This project detects when a person enters a restricted zone in a video using YOLOv5 and OpenCV.
When someone enters the defined zone, an “ALARM” message appears on the screen.

Features:
1. Draw and save a restricted zone from any video frame
2. Detect people entering that zone using YOLOv5
3. Display a visual alarm when a person is inside
4. Simple keyboard control and video playback

Requirements:
Make sure you have Python 3.8+ installed.

Then install the dependencies:
pip install ultralytics opencv-python cvzone numpy yolov5 torchvision torch 

You can use the official instructions for YOLOv5. 
https://github.com/ultralytics/yolov5#installation

How to use:
1. Launch restricted_zone_marking.py, write in terminal "python restricted_zone_marking.py"
2. Mark restricted zone by clicking, press S to save.
3. Launch main.py, write in terminal "python main.py"
