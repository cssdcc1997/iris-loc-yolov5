import torch
import cv2

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5n')  # or yolov5n - yolov5x6, custom

# Images
# img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img = cv2.imread("./data/images/bus.jpg")


# Inference
results = model(img)

# Results
# print(results)
results.show()
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.