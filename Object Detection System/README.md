# Object Detection System

A real-time object detection system built using YOLOv8 and OpenCV. The application detects and classifies objects from a webcam feed and displays the results in real time.

## Objective

The objective of this project is to demonstrate real-time object detection using a pre-trained YOLOv8 model and computer vision techniques.

## Features

* Real-time object detection
* Multi-object detection
* Webcam support
* Bounding boxes and labels
* Pre-trained YOLOv8 model
* Live video processing

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8

## Requirements

```bash id="pw6l3q"
pip install ultralytics opencv-python
```

## Run the Project

```bash id="zrz8ja"
python main.py
```

Press **Q** to close the application.

## How It Works

1. Load the pre-trained YOLOv8 model.
2. Access the webcam using OpenCV.
3. Read video frames continuously.
4. Perform object detection on each frame.
5. Draw bounding boxes and labels.
6. Display the annotated video feed.

## Project Structure

```text id="i4krgm"
Object-Detection-System/
│
├── main.py
├── output.png
└── README.md
```

## Model Information

* Model: YOLOv8 Nano (`yolov8n.pt`)
* Framework: Ultralytics
* Dataset: COCO Dataset
* Supported Classes: 80 object categories

## Concepts Used

* Computer Vision
* Deep Learning
* Object Detection
* Convolutional Neural Networks
* Real-Time Video Processing


## Future Improvements

* Add image file detection.
* Add video file detection.
* Train on custom datasets.
* Save detection results.
* Display confidence scores.
* Build a graphical user interface.
* Deploy as a web application.
  
## Author

**Mahrukh**

Robotics & Intelligence Systems Student passionate about Artificial Intelligence, Machine Learning, Computer Vision, and Software Development.

