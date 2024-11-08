import numpy as np
import cv2
import time
from fastsam import FastSAM, FastSAMPrompt

try:
    model = FastSAM('./weights/FastSAM-x.pt')
except IOError:
    print("Failed to load the FastSAM model.")
    exit()

DEVICE = 'mps'  # Adjust as needed for your hardware
specific_points = [[100, 100]]  
point_labels = [1] 

try:
    cap = cv2.VideoCapture(0)
except IOError:
    print("Failed to open the camera.")
    exit()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame.")
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

    if everything_results and everything_results[0].masks is not None:
        prompt_process = FastSAMPrompt(frame, everything_results, device=DEVICE)
        ann = prompt_process.point_prompt(points=specific_points, pointlabel=point_labels)
        segmented_frame = prompt_process.plot_to_result(frame, annotations=ann)

        end = time.perf_counter()
        total_time = end - start
        fps = 1 / total_time

        cv2.putText(segmented_frame, f'FPS: {int(fps)}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Segmented Frame', segmented_frame)

    else:
        print("No objects detected or no masks available for segmentation.")

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
