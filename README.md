<div align="center">

# 🦯 SafeStep

### Bengala Inteligente para Auxílio à Mobilidade de Pessoas com Deficiência Visual

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![ESP32](https://img.shields.io/badge/Hardware-ESP32-E7352C?style=for-the-badge\&logo=espressif\&logoColor=white)](https://www.espressif.com/)
[![YOLO](https://img.shields.io/badge/Computer%20Vision-YOLO-00FFFF?style=for-the-badge\&logo=yolo\&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Flet](https://img.shields.io/badge/UI-Flet-8B5CF6?style=for-the-badge)](https://flet.dev/)
[![Bluetooth](https://img.shields.io/badge/Communication-Bluetooth%20LE-0082FC?style=for-the-badge\&logo=bluetooth\&logoColor=white)](https://www.bluetooth.com/)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)](https://github.com/giovannibrohrig/SafeStep)

**SafeStep** é um projeto de tecnologia assistiva que combina sensores, comunicação sem fio, visão computacional e síntese de voz para auxiliar pessoas com deficiência visual na identificação de obstáculos durante a locomoção.

[📂 Repositório](https://github.com/giovannibrohrig/SafeStep)

</div>

---

## 📖 Sobre o projeto

O **SafeStep** nasceu como um projeto desenvolvido no curso de **Tecnologia em Inteligência Artificial da FATEC Rio Claro**, com o objetivo de explorar como tecnologias de Inteligência Artificial e sistemas embarcados podem ser utilizadas para aumentar a autonomia e a segurança de pessoas com deficiência visual.

A solução utiliza uma **bengala equipada com sensor ultrassônico**, conectada por **Bluetooth Low Energy (BLE)** a uma aplicação responsável por interpretar os dados recebidos.

Quando um obstáculo é identificado a uma distância próxima, o sistema pode utilizar uma câmera para capturar uma imagem e encaminhá-la para um modelo **YOLO**, que realiza a detecção dos objetos presentes na cena.

As informações identificadas podem então ser transformadas em **feedback de áudio**, permitindo que o usuário receba uma descrição dos elementos encontrados.

### 🎯 Objetivo

Criar uma solução integrada capaz de:

* Detectar obstáculos por meio de sensores;
* Medir a distância até objetos próximos;
* Transmitir informações por Bluetooth Low Energy;
* Identificar objetos utilizando visão computacional;
* Informar ao usuário os objetos encontrados por meio de áudio;
* Integrar hardware, software e Inteligência Artificial em uma solução de tecnologia assistiva.

---

## 🧠 Como funciona

O sistema é dividido em diferentes componentes que trabalham em conjunto:

```text
┌─────────────────────┐
│      BENGALA        │
│       ESP32         │
│                     │
│  Sensor Ultrassônico│
│         ↓           │
│   Medição de        │
│     distância       │
└──────────┬──────────┘
           │
           │ Bluetooth LE
           ▼
┌─────────────────────┐
│     APLICAÇÃO       │
│       Python        │
│                     │
│  Recebe distância   │
└──────────┬──────────┘
           │
           │ distância próxima
           ▼
┌─────────────────────┐
│       CÂMERA        │
│                     │
│  Captura uma imagem │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│        YOLO         │
│                     │
│ Detecção de objetos │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   TEXT-TO-SPEECH    │
│                     │
│   Feedback sonoro   │
└─────────────────────┘
```

### 🔄 Fluxo principal

1. O **ESP32** realiza uma medição utilizando o sensor ultrassônico.
2. A distância é calculada a partir do tempo de retorno do sinal.
3. O ESP32 disponibiliza a distância através de uma característica **BLE**.
4. A aplicação Python utiliza **Bleak** para receber as notificações.
5. Quando a distância recebida fica abaixo do limite configurado, o sistema inicia o processo de análise visual.
6. Uma imagem é capturada pela câmera.
7. O modelo YOLO processa a imagem.
8. Os objetos detectados são identificados.
9. O sistema utiliza **pyttsx3** para transformar a informação em áudio.

---

# 🧩 Arquitetura do projeto

O repositório está organizado em três componentes principais:

```text
SafeStep/
│
├── ESP32/
│   ├── Código do sistema embarcado
│   ├── Comunicação Bluetooth LE
│   ├── Sensor ultrassônico
│   ├── Display OLED
│   └── Buzzer
│
├── Flet/
│   ├── Aplicação de interface
│   ├── Sistema de login
│   ├── Persistência SQLite
│   └── Componentes da aplicação
│
├── Yolo/
│   ├── Treinamento do modelo
│   ├── Inferência em imagens
│   ├── Inferência pela webcam
│   ├── Integração BLE
│   ├── Captura de imagens
│   ├── Reconhecimento de objetos
│   └── Feedback por voz
│
├── WBS_EAP.pdf
├── README.md
└── .gitignore
```

---

# 🔌 Hardware

A parte embarcada do projeto utiliza um **ESP32** para realizar a aquisição e transmissão das informações.

### Componentes identificados no código

| Componente             | Função                                |
| ---------------------- | ------------------------------------- |
| 🧠 ESP32               | Processamento embarcado e comunicação |
| 📡 Sensor ultrassônico | Medição da distância até obstáculos   |
| 📺 OLED SSD1306        | Exibição das informações              |
| 🔊 Buzzer              | Sinalização local                     |
| 📶 Bluetooth LE        | Comunicação entre ESP32 e aplicação   |

### Pinos utilizados

O código atual configura:

| GPIO | Função                            |
| ---: | --------------------------------- |
| `18` | Trigger do sensor ultrassônico    |
| `19` | Echo do sensor ultrassônico       |
|  `5` | Buzzer                            |
| `21` | I²C SDA/SCL conforme configuração |
| `22` | I²C SDA/SCL conforme configuração |

> A montagem física deve seguir o circuito efetivamente utilizado pela equipe. Os pinos acima representam as configurações encontradas no código atual.

---

# 📡 Comunicação Bluetooth LE

A comunicação entre a bengala e a aplicação utiliza **Bluetooth Low Energy**.

O ESP32 disponibiliza um serviço BLE com os seguintes UUIDs:

```text
Service:
a07498ca-ad5b-474e-940d-16f1fbe7e8cd

Characteristic:
51ff12bb-3ed8-46e5-b4f9-d64e2147f29b
```

A aplicação Python utiliza a biblioteca **Bleak** para se conectar ao dispositivo e escutar as notificações da característica.

O dispositivo BLE anunciado pelo ESP32 utiliza o nome:

```text
BengalaInteligente
```

---

# 👁️ Visão Computacional

O módulo de visão computacional utiliza a biblioteca **Ultralytics YOLO**.

O projeto possui:

* Modelo treinado;
* Pesos `.pt`;
* Inferência em imagens;
* Inferência utilizando webcam;
* Pipeline de captura + análise;
* Integração com o sensor da bengala;
* Armazenamento das imagens analisadas.

O modelo treinado atualmente está localizado em:

```text
Yolo/Melhores_treinamentos/train_v5/best.pt
```

Também existe um peso adicional em:

```text
Yolo/weights/yolo26n.pt
```

---

## 🤖 Treinamento

O projeto contém um script de treinamento baseado no Ultralytics:

```text
Yolo/main.py
```

A configuração encontrada utiliza:

```text
Epochs:       400
Image size:   640
Batch size:   16
Optimizer:    SGD
Learning rate: 0.0005
Patience:     40
Device:       GPU
Workers:      8
AMP:          True
```

O treinamento utiliza um dataset configurado no ambiente:

```text
./datasets/blind-assistant-2
```

e salva os resultados no projeto:

```text
SafeStep/
```

---

# 📷 Detecção por imagens

Para executar inferência sobre imagens, o projeto possui:

```text
Yolo/detect_images.py
```

O script carrega o modelo:

```python
YOLO("./Melhores_treinamentos/train_v5/best.pt")
```

e processa as imagens localizadas em:

```text
./imagens_testes
```

Os resultados são salvos em:

```text
./resultados_teste
```

---

# 🎥 Detecção pela webcam

Também existe suporte para inferência utilizando a câmera do computador:

```text
Yolo/detect_webcam.py
```

O modelo é executado diretamente sobre o dispositivo de captura:

```python
model(0, show=True)
```

---

# 🔊 Reconhecimento + feedback de voz

O fluxo integrado está implementado principalmente em:

```text
Yolo/tirar_e_reconhecer_imagens.py
```

Esse módulo combina:

* 📡 Bluetooth LE;
* 📏 Distância do sensor;
* 📷 Webcam;
* 🧠 YOLO;
* 🔊 Text-to-Speech.

O sistema permanece escutando os dados provenientes da bengala.

Quando a distância recebida fica abaixo de:

```text
10 cm
```

o fluxo de reconhecimento é acionado.

A aplicação:

1. Captura uma imagem;
2. Salva a captura temporariamente;
3. Executa o YOLO;
4. Obtém as classes detectadas;
5. Salva a imagem processada;
6. Remove a captura temporária;
7. Gera uma descrição textual;
8. Converte a descrição para áudio através do `pyttsx3`.

Exemplo conceitual do feedback:

```text
Foram identificados, pessoa, cadeira, nessa imagem
```

---

# 🖥️ Aplicação Flet

O diretório `Flet/` contém uma aplicação desenvolvida em **Python + Flet**.

Entre os elementos encontrados estão:

* Tela de login;
* Cadastro de usuários;
* Validação de credenciais;
* Tela principal;
* Persistência de usuários;
* Banco de dados SQLite;
* Interface gráfica.

A aplicação utiliza:

```text
Flet 1.0.2
SQLAlchemy 2.1.1
SQLite
Python 3.14+
```

---

## 🗄️ Banco de dados

A persistência da aplicação utiliza **SQLite** através do SQLAlchemy.

O banco é definido como:

```text
sqlite:///projeto.db
```

A tabela principal encontrada no código é:

```text
Usuario
```

com os campos:

| Campo     | Tipo                  |
| --------- | --------------------- |
| `id`      | Integer / Primary Key |
| `usuario` | String                |
| `senha`   | String                |

> **Nota:** o sistema de autenticação atual é um protótipo. As credenciais são armazenadas diretamente no banco, sem hashing de senha. Essa implementação deve ser reforçada antes de qualquer utilização em ambiente de produção.

---

# 🛠️ Tecnologias

## Software

| Tecnologia          | Utilização                         |
| ------------------- | ---------------------------------- |
| 🐍 Python           | Linguagem principal                |
| 🎯 Ultralytics YOLO | Detecção de objetos                |
| 🔥 PyTorch          | Infraestrutura de Machine Learning |
| 📷 OpenCV           | Captura e processamento de imagens |
| 🗣️ pyttsx3         | Síntese de voz                     |
| 📡 Bleak            | Comunicação BLE                    |
| 🖥️ Flet            | Interface gráfica                  |
| 🗃️ SQLAlchemy      | ORM                                |
| 💾 SQLite           | Persistência local                 |
| ⚡ asyncio           | Programação assíncrona             |

## Hardware / Embedded

| Tecnologia          | Utilização              |
| ------------------- | ----------------------- |
| ESP32               | Microcontrolador        |
| MicroPython         | Programação embarcada   |
| aioble              | Bluetooth Low Energy    |
| SSD1306             | Display OLED            |
| I²C                 | Comunicação com display |
| Sensor ultrassônico | Medição de distância    |

---

# 🚀 Como executar

> O projeto atualmente possui componentes independentes. A configuração abaixo representa os módulos identificados no repositório.

## 1. Clone o repositório

```bash
git clone https://github.com/giovannibrohrig/SafeStep.git
cd SafeStep
```

---

## 2. YOLO

Entre no diretório:

```bash
cd Yolo
```

O projeto possui um `pyproject.toml` e um `uv.lock`.

Com `uv`:

```bash
uv sync
```

ou, dependendo da configuração do ambiente:

```bash
pip install -e .
```

As principais dependências incluem:

```text
ultralytics
torch
torchvision
bleak
opencv
pyttsx3
pynput
keyboard
```

### Executar detecção em imagens

```bash
python detect_images.py
```

### Executar detecção pela webcam

```bash
python detect_webcam.py
```

### Executar o fluxo integrado

```bash
python tirar_e_reconhecer_imagens.py
```

> O fluxo integrado depende de uma câmera funcional, do modelo treinado e de uma bengala ESP32 anunciando o serviço BLE esperado.

---

# ⚡ ESP32

Entre no diretório:

```bash
cd ESP32
```

O código embarcado utiliza MicroPython e bibliotecas como:

```text
aioble
bluetooth
ssd1306
machine
asyncio
```

O script principal de comunicação e medição é:

```text
detect_distance_and_send_with_bluetooth.py
```

Ele:

* Inicializa o sensor ultrassônico;
* Inicializa o display OLED;
* Cria o serviço BLE;
* Anuncia a bengala;
* Mede a distância;
* Envia a distância através da característica BLE.

---

# 🔔 Modo de proximidade

Também existe uma implementação independente para sinalização através de buzzer:

```text
ESP32/buzzer_quando_perto.py
```

Nesse modo, o sistema verifica a distância do obstáculo e utiliza o display para indicar quando algo está próximo.

O limite atualmente implementado nesse script é:

```text
10 cm
```

---

# 📱 Flet

Entre no diretório:

```bash
cd Flet
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

ou utilize o ambiente definido pelo projeto:

```bash
uv sync
```

A aplicação principal está em:

```text
Flet/app.py
```

Para executar:

```bash
python app.py
```

---

# 📂 Estrutura detalhada

```text
SafeStep/
│
├── ESP32/
│   ├── src/
│   │   └── esp32/
│   ├── buzzer_quando_perto.py
│   ├── detect_distance_and_send_with_bluetooth.py
│   ├── installing_mip.py
│   ├── pyproject.toml
│   └── uv.lock
│
├── Flet/
│   ├── src/
│   │   └── safestep_app_flet/
│   ├── app.py
│   ├── main.py
│   ├── models.py
│   ├── projeto.db
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── uv.lock
│
├── Yolo/
│   ├── Melhores_treinamentos/
│   │   └── train_v5/
│   │       └── best.pt
│   │
│   ├── fotos_analisadas/
│   ├── imagens_testes/
│   ├── resultados_teste/
│   ├── weights/
│   │   └── yolo26n.pt
│   │
│   ├── detect_BLE.py
│   ├── detect_images.py
│   ├── detect_webcam.py
│   ├── main.py
│   ├── tirar_e_reconhecer_imagens.py
│   ├── pyproject.toml
│   └── uv.lock
│
├── WBS_EAP.pdf
├── .gitignore
└── README.md
```

---

# 🧪 Estado atual

O SafeStep encontra-se em **desenvolvimento**.

### Implementado no código

* [x] Medição de distância com sensor ultrassônico
* [x] ESP32
* [x] Display OLED
* [x] Buzzer
* [x] Bluetooth Low Energy
* [x] Recepção dos dados BLE em Python
* [x] Captura de imagens pela webcam
* [x] Modelo YOLO treinado
* [x] Detecção de objetos em imagens
* [x] Detecção através da webcam
* [x] Integração entre distância e reconhecimento visual
* [x] Text-to-Speech
* [x] Aplicação Flet
* [x] Persistência local com SQLite

### Em evolução

* [ ] Integração completa entre todos os módulos
* [ ] Refinamento da experiência do usuário
* [ ] Aprimoramento do modelo de visão computacional
* [ ] Melhorias de precisão e desempenho
* [ ] Comunicação mais robusta entre hardware e software
* [ ] Segurança da autenticação
* [ ] Testes automatizados
* [ ] Documentação de montagem do hardware

---

# 🗺️ Roadmap

```text
[x] Protótipo do sensor ultrassônico
[x] Comunicação BLE
[x] Aplicação inicial
[x] Treinamento YOLO
[x] Detecção de objetos
[x] Captura automática de imagens
[x] Feedback por voz
[ ] Integração final dos componentes
[ ] Testes sistemáticos
[ ] Otimização do modelo
[ ] Documentação completa do hardware
[ ] Validação em cenários reais
```

---

# ⚠️ Observações importantes

O SafeStep é um **protótipo acadêmico em desenvolvimento**.

A utilização de uma solução experimental como único mecanismo de auxílio à mobilidade pode apresentar riscos. O sistema não deve ser considerado, em seu estado atual, um substituto para dispositivos ou métodos de orientação e mobilidade profissionalmente validados.

Além disso, algumas partes do projeto ainda possuem características de protótipo, incluindo:

* Credenciais armazenadas diretamente no banco local;
* Dependência de hardware específico;
* Dependência de câmera;
* Dependência do modelo treinado disponível localmente;
* Configurações de BLE específicas;
* Scripts de desenvolvimento ainda em evolução.

---

# 👥 Equipe

Projeto desenvolvido no contexto do curso de **Tecnologia em Inteligência Artificial da FATEC Rio Claro**.

| Integrante          | Área       |
| ------------------- | ---------- |
| **Davi Tonin**      | YOLO       |
| **Giovanni Rohrig** | YOLO       |
| **Gustavo Cruz**    | Lógica     |
| **João Paulo**      | Pareamento |
| **João Pedro**      | Pareamento |
| **João Vitor**      | Lógica     |
| **Juliano Murbach** | Design     |
| **Lucas Batalha**   | Design     |

---

# 📄 Documentação

O repositório também contém documentação relacionada ao planejamento do projeto:

```text
WBS_EAP.pdf
```

Esse material apresenta a estrutura de decomposição do trabalho do projeto.

---

# 🤝 Contribuição

Sugestões, correções e melhorias são bem-vindas.

Para contribuir:

```bash
git clone https://github.com/giovannibrohrig/SafeStep.git
cd SafeStep
```

Crie uma branch para sua alteração:

```bash
git checkout -b feature/minha-feature
```

Faça suas alterações, registre o commit:

```bash
git add .
git commit -m "feat: adiciona minha feature"
```

e envie sua branch:

```bash
git push origin feature/minha-feature
```

Depois, abra um Pull Request no GitHub.

---

# 🔐 Segurança

Caso o projeto evolua para utilização fora do ambiente de prototipagem, recomenda-se revisar especialmente:

* Armazenamento de senhas;
* Gerenciamento de credenciais;
* Segurança da comunicação BLE;
* Validação dos dados recebidos;
* Proteção do banco local;
* Controle de acesso;
* Privacidade das imagens capturadas.

---

# 📜 Licença

**Ainda não definida.**

Até que uma licença seja adicionada ao projeto, os termos de utilização, modificação e redistribuição devem ser considerados conforme os direitos aplicáveis ao código original.

---

<div align="center">

### 🦯 SafeStep

**Tecnologia + Inteligência Artificial + Acessibilidade**

Desenvolvido como projeto acadêmico na
**FATEC Rio Claro**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-SafeStep-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/giovannibrohrig/SafeStep)

</div>
