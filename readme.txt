## ref

- [gitlab page index](https://jiechau.gitlab.io/yolo8custom/index.html)
- [github page index](https://jiechau.github.io/yolo8custom/index.html)
- [gitlab page onnx](https://jiechau.gitlab.io/yolo8custom/index_onnx.html)
- [gitlab page camera](https://jiechau.gitlab.io/yolo8custom/index_camera.html)

- [microsoft](https://microsoft.github.io/onnxjs-demo/#/)
- [yolov8-tfjs](https://hyuto.github.io/yolov8-tfjs/)
- [yolo-coco](https://reu2018dl.github.io/model_coco.html)



## basic

# basic
https://docs.ultralytics.com/zh/models/

# training
https://docs.ultralytics.com/modes/train/




## train your own datasets

# set up env
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

# match the training command:
yolo task=detect mode=train model=yolov8n.pt imgsz=640 data=data.yaml epochs=200 batch=-1 name=yolov8n_custom

# after training, keep the best.pt
cp ./runs/detect/yolov8n_custom4/weights/best.pt .

# run some tests in colab
https://colab.research.google.com/drive/1ggmINPfNywMUHgIDeWkBP0EbrxkaO7VI?usp=sharing


## 

# if clearml https://clear.ml/

# go https://app.clear.ml/projects request credentials
credentials {
	"access_key"="XXXXXXXXXXXX"
	"secret_key"="YYYYYYYYYYYYYYYYYYYYYYYY"
}
# run
pip install clearml
clearml-init



## datasets

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


##

# onnx

- [microsoft](https://microsoft.github.io/onnxjs-demo/#/)
- [yolov8-tfjs](https://hyuto.github.io/yolov8-tfjs/)
- [yolo-coco](https://reu2018dl.github.io/model_coco.html)

# onnx js reference
https://github.com/akbartus/Yolov8-Object-Detection-on-Browser/blob/main/yolov8_onnx_without_nms/index.html



# ref
https://learnopencv.com/train-yolov8-on-custom-dataset/

其他
https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993


基本安裝 ultralytics
https://docs.ultralytics.com/zh/models/#featured-models
onnx
https://docs.ultralytics.com/zh/integrations/onnx/#onnx-and-onnx-runtime
onnx browser
https://github.com/akbartus/Yolov8-Object-Detection-on-Browser/tree/main


訓練自訂模型
https://medium.com/@EricChou711/yolov8-%E4%BB%8B%E7%B4%B9%E5%92%8C%E6%89%8B%E6%8A%8A%E6%89%8B%E8%A8%93%E7%B7%B4%E8%87%AA%E8%A8%82%E7%BE%A9%E6%A8%A1%E5%9E%8B-752d8d32cb73

bus picture:
https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/bus.jpg


