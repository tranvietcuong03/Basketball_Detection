# Basketball Object Detection
![YOLOv5](https://img.shields.io/badge/YOLOv5-%23013243.svg?style=for-the-badge&logo=YOLOv5&logoColor=white)

## Introduction
I clone YOLOv5 to train my custom dataset about Basketball object. 

## Demo
*Detect Objects in some Basketball scenes:
![..](https://github.com/tranvietcuong03/Basketball_Detection/blob/master/Visualize/image.png). 

*Link demo with a Basketball sample short: [Link to video](https://youtu.be/aNOFAVKMyoE).

## Dataset
[Download here](https://github.com/tranvietcuong03/Basketball_Detection/tree/master/Basketball). 

# Review
*There are some training progress notes:
![...](https://github.com/tranvietcuong03/Basketball_Detection/blob/master/Visualize/tensorboard_1.png)

![...](https://github.com/tranvietcuong03/Basketball_Detection/blob/master/Visualize/tensorboard_2.png).

![...](https://github.com/tranvietcuong03/Basketball_Detection/blob/master/runs/train/exp/PR_curve.png).

*It has more informative number after training on 30 epochs saved in **result.csv** file ([Link to file](https://github.com/tranvietcuong03/Basketball_Detection/blob/master/runs/train/exp/results.csv) )

## Requirements
In this project, I clone the YOLOv5 and training with my custom dataset. <br>
*Clone YOLOv5
```sh
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
  ```
*Training
```sh
python train.py --data dataset.yaml --img 640 --epochs 30 --batch-size 8 --weights yolov5n.pt
  ```
*Inference <br>
1. Test image
```sh
python detect.py --weights runs/train/exp/weights/best.pt --source Basketball/test/images
  ```
2. Test video
```sh
python detect.py --weights runs/train/exp/weights/best.pt --source Basketball/video
  ```
