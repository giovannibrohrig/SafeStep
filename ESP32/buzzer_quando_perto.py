import time
from machine import Pin, time_pulse_us


trig = Pin(19, Pin.OUT)
echo = Pin(21, Pin.IN)
buzzer = Pin(5, Pin.OUT)

trig.off()
buzzer.on()
time.sleep_ms(20)

while True:
    trig.on()
    time.sleep_ms(10)
    trig.off()
    
    duracao = time_pulse_us(echo, 1, 30000)
    
    if duracao > 0:
        distancia = (duracao*0.0343)/2
        if distancia < 10:
            buzzer.off()
            print(f"Distancia: {distancia:.2f}")
        else:
            buzzer.on()
            print("nada perto")
    else:
        print("Erro, Algo deu errado")
    
    
    time.sleep_ms(500)