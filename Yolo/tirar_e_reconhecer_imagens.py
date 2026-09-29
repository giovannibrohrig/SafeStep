import os
import cv2
from datetime import datetime
from ultralytics import YOLO
import keyboard
import sys
import shutil
import pyttsx3

def tirar_foto():
    pasta_destino="fotos_analise_pendente"
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"captura_{timestamp}.jpg"

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Camera não encontrada")
        return None

    print("Se prepare para a foto")
    cv2.waitKey(2000)

    sucesso , frame = camera.read()

    camera.release()

    if sucesso:
        caminho_final = os.path.join(pasta_destino, nome_arquivo)
        cv2.imwrite(caminho_final, frame)
        print(f"Foto salva: {caminho_final}")
        return True
    else:
        print("Falha na captura")
        return None
model = YOLO("./Melhores_treinamentos/train_v5/best.pt")
def analisar_foto():


    results = model("./fotos_analise_pendente", verbose=False)
    diretorio_destino = "./fotos_analisadas"

    labels_detectadas = []

    # CORREÇÃO: Itera sobre cada imagem processada na lista
    for resultado in results:
        # Agora sim acessamos o .names e o .boxes de CADA imagem
        dicionario_nomes = resultado.names

        for box in resultado.boxes:
            id_classe = int(box.cls.item())
            nome_classe = dicionario_nomes[id_classe]

            # Adiciona na lista global se ainda não estiver nela
            if nome_classe not in labels_detectadas:
                labels_detectadas.append(nome_classe)

        nome_original = os.path.basename(resultado.path)
        caminho_completo = os.path.join(diretorio_destino, nome_original)
        resultado.save(filename=caminho_completo)
    if os.path.exists("./fotos_analise_pendente"):
        shutil.rmtree("./fotos_analise_pendente")
    os.makedirs("./fotos_analise_pendente")
    return labels_detectadas


def app():
    while True:
        while True:
            print("Aperte Enter para tirar foto, ou ESPAÇO para sair")
            event = keyboard.read_event()

            if  event.event_type == keyboard.KEY_DOWN:
                if event.name == 'enter':
                    break
                elif event.name == 'space':
                    sys.exit()
        foto = tirar_foto()
        if foto:
            print("Aperte ENTER para analisar a imagem")
            keyboard.wait('enter')
            labels = analisar_foto()
            labels = ", ".join(labels)
            texto = f"Foram identificados, {labels}, nessa imagem"
            print(texto)
            motor = pyttsx3.init()
            motor.say(texto)
            motor.runAndWait()
        else:
            print("algo deu errado")
            break



app()




