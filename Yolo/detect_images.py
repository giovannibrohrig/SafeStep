from ultralytics import YOLO
import os

model = YOLO("./Melhores_treinamentos/train_v5/best.pt")

results = model("./imagens_testes")
diretorio_destino = "./resultados_teste"


for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    obb = result.obb
    # result.show()
    nome_original = os.path.basename(result.path)
    caminho_completo = os.path.join(diretorio_destino, nome_original)
    result.save(filename=caminho_completo)


os.startfile(os.path.abspath("./resultados_teste"))
