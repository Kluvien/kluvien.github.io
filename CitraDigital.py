!pip install ultralytics
!pip install matplotlib opencv-python-headless
!pip install roboflow

import matplotlib.pyplot as plt
from ultralytics import YOLO
from google.colab import files
import cv2
import numpy as np
import os

from roboflow import Roboflow
rf = Roboflow(api_key="ZNqeAZVNO6OK6SBwJP6m")
project = rf.workspace("front").project("deteksi-anime-yt9cz")
version = project.version(2)
dataset = version.download("yolov8")


dataset_location = dataset.location
print("Dataset downloaded to:", dataset_location)


model = YOLO("yolov8n.pt")
model.train(data="/content/deteksi-anime-2/data.yaml", epochs=25, imgsz=320)
model = YOLO("/content/runs/detect/train/weights/best.pt")
dataset = version.download("yolov8")

image_path = "/content//content/Screenshot 2023-08-15 205416.png"
gray_image_path = "/content/Screenshot 2023-08-15 205416_gray.png"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(gray_image_path, gray_image)
result = model.predict(source="/content/Screenshot 2023-08-15 205416.png", imgsz=640, save=True)


image_result = result[0]

for box in image_result.boxes.data:
    x_min, y_min, x_max, y_max, confidence, class_id = box.tolist()
    print(f"Bounding Box: ({x_min:.2f}, {y_min:.2f}, {x_max:.2f}, {y_max:.2f})")
    print(f"Confidence: {confidence:.2f}")
    print(f"Class ID: {int(class_id)}")

total_bounding_boxes = len(image_result.boxes.data)
print(f"Total Bounding Boxes: {total_bounding_boxes}")

from IPython.display import Image, display
image_path_with_predictions = image_result.plot()

import matplotlib.pyplot as plt
plt.imshow(image_path_with_predictions)
plt.axis("off")
plt.show()


img = cv2.imread("/content/gol2.png")

for box in image_result.boxes.data:
    x_min, y_min, x_max, y_max, confidence, class_id = box.tolist()
    x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)

    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    label = f"Class: {int(class_id)}, Conf: {confidence:.2f}"
    cv2.putText(img, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

!ls runs/detect/predict
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
model = YOLO('yolov8n.pt')
results = model(image_path)
annotated_img = results[0].plot()
cv2.imwrite("runs/detect/predictions.jpg", annotated_img)

plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("YOLO Detected Objects")
plt.show()
