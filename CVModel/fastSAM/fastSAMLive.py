from fastsam import FastSAM
import numpy as np
import cv2
import time


# Load the model
model = FastSAM('./weights/FastSAM-x.pt')

DEVICE = 'mps'

try:
    cap = cv2.VideoCapture(0)
except IOError:
    print("Failed to open the camera.")


while cap.isOpened():
    
    suc, frame = cap.read()
    if not suc:
        print("failed to grab frame")
        break
    
    start = time.perf_counter()
    

    everything_results = model(
        source=frame,
        device=DEVICE,
        retina_masks=True,
        imgsz=1024,
        conf=0.4,
        iou=0.9,
    )
    
    print(everything_results[0].masks.shape)
    print(everything_results[0].boxes.shape)
    print(everything_results[0].boxes[0].xyxy.cpu().numpy())
    if everything_results and everything_results[0].boxes is not None:
        for box in everything_results[0].boxes:

            box_coords = box.xyxy.cpu().numpy()[0]
            print(box)
            cv2.rectangle(frame, (int(box_coords[0]), int(box_coords[1])), 
                        (int(box_coords[2]), int(box_coords[3])), 
                        (0, 255, 0), 2)
    else:
        print("No objects detected in this frame.")
    
    end = time.perf_counter()
    total_time = end - start
    fps = 1 / total_time
    cv2.putText(frame, f'FPS: {int(fps)}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Segmented frame', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()