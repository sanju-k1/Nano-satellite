import machine
import utime
from chittiSat.pressure import*
from chittiSat.assistant import*

i2c=machine.I2C(0, scl = machine.Pin(1), sda = machine.Pin(0))

devices = i2c.scan()

if devices:
    print(devices)
    
    
bmp280 = BMP280(i2c)
calibrate.pressure(bmp280)

utime.sleep(2)

while True:
 Pressure = bmp280.pressure
 temperature = bmp280.temperature
 dashboard.sendpressure(Pressure,temperature)
 utime.sleep(1) 