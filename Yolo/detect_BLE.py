# Arquivo:名 bengala_ble.py
import asyncio
from bleak import BleakClient

ENDERECO_MAC = "14:33:5C:6B:B5:96"
UUID_CARACTERISTICA = "51ff12bb-3ed8-46e5-b4f9-d64e2147f29b"


async def escutar_bengala():
    fila_dados = asyncio.Queue()

    def callback_notificacao(sender, data):
        try:
            texto = data.decode('utf-8')
            fila_dados.put_nowait(texto)
        except UnicodeDecodeError:
            pass

    print(f"Tentando conectar ao dispositivo {ENDERECO_MAC}...")

    async with BleakClient(ENDERECO_MAC, timeout=15.0, cache_mode="disabled") as client:
        if client.is_connected:
            print(" Conectado com sucesso!")
            print("Estabilizando conexão...")
            await asyncio.sleep(1.5)

            print(f" Ativando escuta para: {UUID_CARACTERISTICA}")
            await client.start_notify(UUID_CARACTERISTICA, callback_notificacao)
            print("Aguardando atualizações do sensor...\n")

            while True:
                dado_recebido = await fila_dados.get()
                yield dado_recebido  # Envia o dado para quem importou esta função
