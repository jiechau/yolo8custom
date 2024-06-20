from ultralytics import YOLO

# Load the YOLOv8 model
#model = YOLO("yolov8n.pt")
model = YOLO("./best.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates 'yolov8n.onnx'

# Load the exported ONNX model
#onnx_model = YOLO("yolov8n.onnx")

# Run inference
url = "https://ultralytics.com/images/bus.jpg" # 4 persion, 1 bus
url = 'https://img.shopping.friday.tw/images/product/289/8686719/8686719_3_1.webp' # 1 female 1 male
results = model(url)
