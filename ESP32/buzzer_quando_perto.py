import time
from machine import Pin, time_pulse_us, I2C
import ssd1306


trig = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)
buzzer = Pin(5, Pin.OUT)
i2c = I2C(0, scl=Pin(21), sda=Pin(22), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

largura = 128
altura = 64

oled = ssd1306.SSD1306_I2C(largura, altura, i2c)
oled.fill(0)

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
            oled.fill(0)
            oled.text(f"Distancia: {distancia:.2f}", 0, 20)
            print(f"Distancia: {distancia:.2f}")
            oled.show()
        else:
            oled.fill(0)
            oled.text("nada perto", 0, 30)
            print("nada perto")
            oled.show()
    else:
        print("Erro, Algo deu errado")
    
    
    time.sleep_ms(500)