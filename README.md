# Customized Fast Segment Anything Model and YOLOv8 Protocol Error Detection Model

## **Project Overview**
This project is designed to **detect human-prone errors** in labware setup during protocol execution on the **Opentrons OT-2** robot. Due to the similar appearance of many labware types, mistakes are common. The system leverages AI models for **real-time error detection** through video segmentation and object classification.

---

## **AI Workflow**
The AI-driven solution involves two main tasks:
1. **Video Segmentation:**  
   Segmenting the OT-2 protocol deck and extracting cropped images of labware.
2. **Labware Classification:**  
   Classifying segmented labware and identifying incorrect placements.

---

## **Implementation Details**

### **Initial Approach**
- **Model:** Segment Anything Model 2 (SAM2) by Meta.  
- **Purpose:** Real-time segmentation of the OT-2 protocol deck.  
- **Outcome:**  
  - Achieved high segmentation accuracy.  
  - Computationally expensive; required **A100 GPUs**.

### **Optimized Approach**
- **Model:** FastSAM (a lightweight version of SAM2).  
- **Purpose:** Efficient video segmentation with reduced computational cost.  
- **Enhancements:**  
  - Trained a **YOLOv8** model on **T4 GPUs** for labware classification.  
  - Stored YOLOv8 weights locally for fast inference.  
  - Integrated **FastSAM** and **YOLOv8** in a Python script for real-time error detection using a laptop webcam.

---

## **Real-World Deployment**
- Developed a **real-time error detection system** using a laptop webcam.
- Ongoing integration with a **fixed webcam** for continuous monitoring on lab computers.

---

## **Tech Stack**
- **FastSAM:** Lightweight video segmentation model.
- **YOLOv8:** Object detection and classification.
- **OpenCV:** Video capture and image processing.
- **PyTorch:** Deep learning framework for model training and inference.
- **NumPy:** Data handling and array manipulation.
- **Python:** Scripting for model integration and real-time detection.

---

## **Project Structure**
### **`CVModel/`**
Contains all computer vision-related implementations:
- **`SAM2/`**: Initial implementation using SAM2 for video segmentation.
- **`FastSAM/`**: Current implementation using FastSAM for efficient segmentation.  
  - Includes the Python script for labware segmentation. Refer to instructions above for details on running the script.

### **`Protocols/`**
Contains a series of Python pooling protocols designed to improve liquid handling efficiency:
- Optimized protocols achieve a **95% efficiency** rate in liquid handling.  
- Detailed documentation on these protocols can be found in the README file within this folder.

---

## **Future Work**
- Finalize the integration of a **fixed webcam** for lab monitoring.  
- Expand the system to handle additional labware types or other protocol errors.  
- Further optimize the workflow for broader scalability.

---

## **Getting Started**
### **Clone the Repository**
```bash
git clone https://github.com/4n4ny4/Opentrons
cd CVModel/FastSAM
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Run real-time detection of latest developed model (fastSAM/Yolov8)
```bash
python detect_labware_errors.py
```
