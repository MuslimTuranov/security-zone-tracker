import cv2
import json
import numpy

cap = cv2.VideoCapture("test.mp4")

zone_points = []

def draw_zone(event, x, y, flags, param):
    global zone_points
    if event == cv2.EVENT_LBUTTONDOWN:
        zone_points.append((x, y))
        print(f"Point added: {(x, y)}")

cv2.namedWindow("Mark Zone")
cv2.setMouseCallback("Mark Zone", draw_zone)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for point in zone_points:
        cv2.circle(frame, point, 5, (0,255,0), -1)

    if len(zone_points) >= 2:
        cv2.polylines(frame, [numpy.array(zone_points)], isClosed=True, color=(0,255,0), thickness=2)

    cv2.imshow("Mark Zone", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'): 
        break
    elif key == ord('s'):  
        with open("restricted_zones.json", "w") as f:
            json.dump([{"points": zone_points}], f)
        print("Zone saved to restricted_zones.json")
        break

cap.release()
cv2.destroyAllWindows()
