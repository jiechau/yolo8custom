# ref
https://learnopencv.com/train-yolov8-on-custom-dataset/

## 

# basic
https://docs.ultralytics.com/zh/models/

# training
https://docs.ultralytics.com/modes/train/



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



##

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