import cv2
from fastsam import FastSAM, FastSAMPrompt
from ultralytics import YOLO
import numpy as np

# Load the models
model = FastSAM('FastSAM-x.pt')
YOLOmodel = YOLO('testingbest.pt')  # current best YOLOv8 model that I trained
DEVICE = 'cpu'  

cap = cv2.VideoCapture(0)  

# Set a frame limit for demonstration (remove this to run indefinitely)
max_frames = 1  

user_clicks = []
point_confirmed = False


def mouse_callback(event, x, y, flags, param):
    """Callback function to handle mouse clicks."""
    global user_clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        user_clicks.append((x, y))
        print(f"Point added: {x, y}")


# Create a window for display and set mouse callback
cv2.namedWindow("Frame Preview")
cv2.setMouseCallback("Frame Preview", mouse_callback)

# Loop through each frame from the webcam
while cap.isOpened() and max_frames > 0:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from webcam. Exiting.")
        break

    # Display the frame with user clicks overlaid
    preview_frame = frame.copy()
    for point in user_clicks:
        cv2.circle(preview_frame, point, 5, (0, 0, 255), -1) 

    cv2.putText(preview_frame, "Click to place points. Press 'c' to confirm or 'q' to quit.", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("Frame Preview", preview_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):  
        point_confirmed = True
        break
    elif key == ord('q'): 
        print("Exiting.")
        break

if point_confirmed and user_clicks:
    detected_objects = []

    frame_path = 'temp_frame.jpg'
    cv2.imwrite(frame_path, frame)

    # Apply FastSAM to generate masks for each user click
    everything_results = model(frame_path, device=DEVICE, retina_masks=True, imgsz=1024, conf=0.4, iou=0.9)
    prompt_process = FastSAMPrompt(frame_path, everything_results, device=DEVICE)

    for idx, point_coords in enumerate(user_clicks):
        point_labels = [1] 
        ann = prompt_process.point_prompt([point_coords], point_labels)
        mask = ann[0]

        # Save the mask
        mask_path = f'mask_{idx + 1}.png'
        cv2.imwrite(mask_path, mask.astype(np.uint8) * 255)  

        # Find the bounding box of the mask
        y_indices, x_indices = mask.nonzero()
        if len(y_indices) > 0 and len(x_indices) > 0:  
            x_min, x_max = int(x_indices.min()), int(x_indices.max())
            y_min, y_max = int(y_indices.min()), int(y_indices.max())


            cropped_frame = frame[y_min:y_max, x_min:x_max]


            cropped_frame_path = f'cropped_frame_{idx + 1}.jpg'
            cv2.imwrite(cropped_frame_path, cropped_frame)

            # Detect objects using YOLOv8
            img = cv2.imread(cropped_frame_path) 
            results = YOLOmodel(img)
            for box in results[0].boxes:
                class_idx = int(box.cls)
                confidence = box.conf.item()
                xyxy = box.xyxy.numpy()
                class_name = results[0].names[class_idx]

                detected_objects.append({
                    "object": class_name,
                    "confidence": confidence,
                    "bounding_box": xyxy.tolist()
                })


cap.release()
cv2.destroyAllWindows()

# Output the results
if detected_objects:
    print("\nDetected Objects and Bounding Boxes:")
    for idx, obj in enumerate(detected_objects):
        print(f"{idx + 1}. Object: {obj['object']}, Confidence: {obj['confidence']:.2f}, Bounding Box: {obj['bounding_box']}")
else:
    print("No objects detected.")
