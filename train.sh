#!/bin/bash
yolo task=detect mode=train model=yolov8n.pt imgsz=640 data=data.yaml epochs=200 batch=-1 name=yolov8n_custom

