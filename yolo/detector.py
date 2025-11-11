def run_detector():
    import cv2
    from ultralytics import YOLO
    import cvzone
    import json
    import numpy 

    cap = cv2.VideoCapture("test.mp4")

    with open('restricted_zones.json') as f:
        restricted_zones = json.load(f)

    zone_points = numpy.array(restricted_zones[0]["points"])

    model = YOLO("yolov5su.pt")

    def is_inside_zone(box, zone_points):
        x1, y1, x2, y2 = box
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        return cv2.pointPolygonTest(zone_points, (cx, cy), False) >= 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.track(frame, persist=True)

        cv2.polylines(frame, [zone_points], isClosed=True, color=(0,0,255), thickness=2)

        if results[0].boxes is not None and results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.int().cpu().tolist()
            class_ids = results[0].boxes.cls.int().cpu().tolist()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            confidences = results[0].boxes.conf.cpu().tolist()

            for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
                c = model.names[class_id]  
                x1, y1, x2, y2 = box
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cvzone.putTextRect(frame,f'{track_id}',(x1,y1),1,1)

                if c == "person" and is_inside_zone(box, zone_points):
                    cvzone.putTextRect(frame, "ALARM!", (50, 50), scale=2, thickness=2, colorR=(0,0,255))

        cv2.imshow("RGB", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
