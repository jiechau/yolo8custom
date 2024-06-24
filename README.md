
## yolov8 nano onnx version

- [Object Detection with Webcam/Mobile Camera in live streaming](https://jiechau.gitlab.io/yolo8custom/index.html)
- switch model: default yolo8vn (coco 2017 dataset), yolov8n-oiv7 (open images v7 dataset), women-men (2022 dataset)
- FPS can be a decimal number, for example, 0.3 means 1 frame every 3 seconds.


other quick links and reference:<br/>

- [gitlab page onnx](https://jiechau.gitlab.io/yolo8custom/index_onnx.html)
- [gitlab page camera](https://jiechau.gitlab.io/yolo8custom/index_camera.html)
- [gitlab page index](https://jiechau.gitlab.io/yolo8custom/index.html)
- [github page index](https://jiechau.github.io/yolo8custom/index.html)

- [microsoft](https://microsoft.github.io/onnxjs-demo/#/)
- [yolov8-tfjs](https://hyuto.github.io/yolov8-tfjs/)
- [yolo-coco](https://reu2018dl.github.io/model_coco.html)

<br/>

# train your own datasets

## set up env
```bash
/usr/local/bin/python3.9 -m venv --system-site-packages py39yolo8custom
source py39yolo8custom/bin/activate
pip install --upgrade pip
pip install ultralytics
# there is a datasets_dir config
vi /home/jiechau/.config/Ultralytics/settings.yaml
datasets_dir: /home/jiechau/datasets

# download women-men dataset from roboflow
https://universe.roboflow.com/generalstuff/women-men/dataset/1/download/yolov8

# unzip it and make dataset this structure:
/home/jiechau/datasets/women-men
/home/jiechau/datasets/women-men/train
/home/jiechau/datasets/women-men/train/images
/home/jiechau/datasets/women-men/train/labels
/home/jiechau/datasets/women-men/valid
/home/jiechau/datasets/women-men/valid/images
/home/jiechau/datasets/women-men/valid/labels
/home/jiechau/datasets/women-men/test
/home/jiechau/datasets/women-men/test/images
/home/jiechau/datasets/women-men/test/labels

# so that 
# our data.yaml looks like this
train: women-men/train/images
val: women-men/valid/images
test: women-men/test/images
nc: 2
names: ['Female', 'Male']

# because in /home/jiechau/.config/Ultralytics/settings.yaml
datasets_dir: /home/jiechau/datasets
```

## train/fine-tune yolov8n
```bash
# the training command:
yolo task=detect mode=train model=yolov8n.pt imgsz=640 data=data.yaml epochs=200 batch=-1 name=yolov8n_custom

# after training, keep the best.pt
cp ./runs/detect/yolov8n_custom4/weights/best.pt .
```

convert to onnx
```
from ultralytics import YOLO
model = YOLO("./best.pt")
model.export(format="onnx")  # creates 'best.onnx'
```

## run some tests in colab
```
# having best.pt
https://colab.research.google.com/drive/1ggmINPfNywMUHgIDeWkBP0EbrxkaO7VI?usp=sharing
```


## if clearml https://clear.ml/
```
# go https://app.clear.ml/projects request credentials
credentials {
	"access_key"="XXXXXXXXXXXX"
	"secret_key"="YYYYYYYYYYYYYYYYYYYYYYYY"
}
```

```
# run
pip install clearml
clearml-init
```


## basic memo/reference

```
# basic
https://docs.ultralytics.com/zh/models/

# training
https://docs.ultralytics.com/modes/train/
```

## datasets memo/refrernce
```
# some other dataset and reference:

# https://learnopencv.com/train-yolov8-on-custom-dataset/
# download pothole
wget https://www.dropbox.com/s/qvglw8pqo16769f/pothole_dataset_v8.zip?dl=1
# https://github.com/spmallick/learnopencv/blob/master/Train-YOLOv8-on-Custom-Dataset-A-Complete-Tutorial/yolov8_fine_tuning.ipynb

# roboflow women-men
https://universe.roboflow.com/generalstuff/women-men/dataset/1/download/yolov8

# download kaggle (but no boundary box mark)
pip install -q kaggle
kaggle datasets download -d playlist/men-women-classification
```