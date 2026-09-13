from ultralytics import YOLO
#from roboflow import Roboflow

model = YOLO('../runs/detect/SafeStep/train_v5/weights/best.pt')

results = model.train(
    data='./datasets/blind-assistant-2',
    epochs=400,
    imgsz=640,
    batch=16,
    optimizer='SGD',
    lr0=0.0005,
    patience=40,
    device=0,
    workers=8,
    cache=True,
    amp=True,
    save_period=10,
    project='SafeStep',
    name='train_v5_ft_v2'
)

