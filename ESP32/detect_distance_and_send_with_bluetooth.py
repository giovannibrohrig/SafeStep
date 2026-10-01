import aioble
import bluetooth
import asyncio
import time
from machine import Pin, time_pulse_us

trig = Pin(19, Pin.OUT)
echo = Pin(21, Pin.IN)

trig.off()
time.sleep_ms(20)


_TEMP_SERVICE_UUID = bluetooth.UUID("a07498ca-ad5b-474e-940d-16f1fbe7e8cd")
_TEMP_CHAR_UUID    = bluetooth.UUID("51ff12bb-3ed8-46e5-b4f9-d64e2147f29b")

# Appearance: 0x0300 = Generic Thermometer (optional, helps phone apps)
_ADV_APPEARANCE_THERMOMETER = const(0x0300)

temp_service = aioble.Service(_TEMP_SERVICE_UUID)
temp_char = aioble.Characteristic(
    temp_service,
    _TEMP_CHAR_UUID,
    read=True,
    notify=True,
)
aioble.register_services(temp_service)

_ADV_INTERVAL_US = 250_000  # 250 ms

async def peripheral_task():
    while True:
        async with await aioble.advertise(
            _ADV_INTERVAL_US,
            name="BengalaInteligente",
            services=[_TEMP_SERVICE_UUID],
            appearance=_ADV_APPEARANCE_THERMOMETER,
        ) as connection:
            print("Central connected:", connection.device)
            await connection.disconnected(timeout_ms=None)
            print("Disconnected")
            
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
            temp_char.write("{:.1f}".format(distancia), send_update=True)
            
        else:
            print("Erro, Algo deu errado")   
        await asyncio.sleep_ms(1000)

async def main():
    await asyncio.gather(distance_sensor(), peripheral_task())

asyncio.run(main())