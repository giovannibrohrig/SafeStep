import aioble
import bluetooth
import asyncio
import time
from machine import Pin, time_pulse_us, I2C
import ssd1306

i2c = I2C(0, scl=Pin(21), sda=Pin(22), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

largura = 128
altura = 64

oled = ssd1306.SSD1306_I2C(largura, altura, i2c)
oled.fill(0)

trig = Pin(18, Pin.OUT)
echo = Pin(19, Pin.IN)

trig.off()
time.sleep_ms(20)


_DIST_SERVICE_UUID = bluetooth.UUID("a07498ca-ad5b-474e-940d-16f1fbe7e8cd")
_DIST_CHAR_UUID    = bluetooth.UUID("51ff12bb-3ed8-46e5-b4f9-d64e2147f29b")



dist_service = aioble.Service(_DIST_SERVICE_UUID)
dist_char = aioble.Characteristic(
    dist_service,
    _DIST_CHAR_UUID,
    read=True,
    notify=True,
)
aioble.register_services(dist_service)

_ADV_INTERVAL_US = 250_000  # 250 ms

def show_on_screen(text):
    text = str(text)
    oled.fill(0)
    oled.text(text)
    oled.show
async def peripheral_task():
    while True:
        async with await aioble.advertise(
            _ADV_INTERVAL_US,
            name="BengalaInteligente",
            services=[_DIST_SERVICE_UUID],
        ) as connection:
            print("Central connected:", connection.device)
            text = f"Central connected: {connection.device}"
            show_on_screen(text)
            await connection.disconnected(timeout_ms=None)
            print("Disconnected")
            show_on_screen("Disconnected")           
import random

async def distance_sensor():
    while True:
        trig.on()
        time.sleep_ms(10)
        trig.off()
        
        duracao = time_pulse_us(echo, 1, 30000)
        
        if duracao > 0:
            distancia = (duracao*0.0343)/2
            
            print(f"Distancia: {distancia:.2f}")
            text = f"Distancia: {distancia:.2f}"
            show_on_screen(text)
            dist_char.write("{:.1f}".format(distancia), send_update=True)
            
        else:
            print("Erro, Algo deu errado")
            show_on_screen("Erro, algo deu errado")
        await asyncio.sleep_ms(1000)

async def main():
    await asyncio.gather(distance_sensor(), peripheral_task())

print("Aguardando estabilização de energia")
show_on_screen("Aguardando estabilização de energia")
time.sleep(2)
asyncio.run(main())