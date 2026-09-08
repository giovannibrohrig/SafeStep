from ultralytics import YOLO

model = YOLO('yolo26n.pt')

results = model.train(
    data="C:/Users/Aluno/Downloads/blind assistant.v2i.yolo26",
    epochs=20,
    imgsz=416,
    batch=4,
    optimizer='SGD',
    lr0=0.01,
    patience=30,
    device='cpu',
    workers=2,
    project='SafeStep',
    name='train_v1'
)

metrics = model.val()
metrics.box.maps