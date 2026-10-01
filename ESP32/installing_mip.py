import network
import time
import machine
import mip

def conectar_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    
    # CORREÇÃO: Força o desligamento para resetar o estado interno do rádio
    print("Resetando interface Wi-Fi...")
    wlan.active(False)
    time.sleep(1) 
    wlan.active(True)
    
    # Se por algum motivo já estiver conectado, não chama o .connect() de novo
    if wlan.isconnected():
        print("Já estava conectado!")
        print(wlan.ifconfig())
        return

    print("Conectando ao Wi-Fi...")
    try:
        wlan.connect(ssid, password)
    except OSError as e:
        print(f"Erro inicial ao conectar: {e}")
        print("Reiniciando a placa em 3 segundos...")
        time.sleep(3)
        machine.reset() # Hard reset se o chip travar totalmente

    # Aguarda até conectar
    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        print(".", end="")
        time.sleep(1)
        timeout -= 1
            
    if wlan.isconnected():
        print("\nConectado com sucesso!")
        print("Configuração de rede:", wlan.ifconfig())
    else:
        print("\nFalha por timeout. Verifique o sinal, SSID e a senha.")

# Teste novamente
conectar_wifi("sopa", "12345678")

mip.install("aioble")





