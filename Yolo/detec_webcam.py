from ultralytics import YOLO

model = YOLO("../Melhores_treinamentos/train_v5/best.pt")

results = model(0, show=True)