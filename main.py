import cv2
from ultralytics import YOLO 
import torch
model = YOLO("yolov5s.pt") 
cap = cv2.VideoCapture("test.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)  
    annotated_frame = results[0].plot()  
    cv2.imshow("YOLO Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
