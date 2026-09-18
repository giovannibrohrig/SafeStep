from ultralytics import YOLO

model = YOLO("./Melhores_treinamentos/train_v5/best.pt")

results = model(["image1.jpeg", "image2.jpeg"])


for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    obb = result.obb
    result.show()
    result.save()