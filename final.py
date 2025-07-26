import machine
import utime
import uos

from chittiSat.mq2 import MQ2
from chittiSat.gyro import MPU6050
from chittiSat.pressure import *
from chittiSat.assistant import *
from chittiSat.sdcard import *

# i2c configuration
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
devices = i2c.scan()
if devices:
    print(devices)

# mq2
sensor = MQ2(pinData=26)
sensor.calibrate()

# gyro
mpu6050 = MPU6050(i2c)

#pressure
bmp280 = BMP280(i2c)
calibrate.pressure(bmp280)

# Sdcard
spi = machine.SPI(1, sck=machine.Pin(14), mosi=machine.Pin(15), miso=machine.Pin(12))
sd = SDCard(spi)
uos.mount(sd, '/sd')
print("sd card connected")
print(uos.listdir('/sd'))

# Define the newFile function
def newFile(existing_files):
    # Creating a new file name based on existing files
    base_name = "data"
    extension = ".csv"
    counter = 1
    while True:
        new_name = f"{base_name}_{counter}{extension}"
        if new_name not in existing_files:
            return f"/sd/{new_name}"
        counter += 1

# Creating file name
myfile = newFile(uos.listdir('/sd'))

with open(myfile, "w") as f:
    f.write("Time")
    f.write(",")

    f.write("Pressure")
    f.write(",")

    f.write("temperature")
    f.write(",")

    f.write("Smoke")
    f.write(",")

    f.write("LPG")
    f.write(",")

    f.write("Methane")
    f.write(",")

    f.write("Hydrogen")
    f.write(",")

    f.write("Ax")
    f.write(",")

    f.write("Ay")
    f.write(",")

    f.write("Az")
    f.write(",")

    f.write("Gx")
    f.write(",")

    f.write("Gy")
    f.write(",")

    f.write("Gz")
    f.write(",")

    f.write("\n")

    while True:
        t = utime.ticks_ms() / 1000
        

        Pressure = bmp280.pressure
        temperature = bmp280.temperature

        Smoke = sensor.readSmoke()
        LPG = sensor.readLPG()
        Methane = sensor.readMethane()
        Hydrogen = sensor.readHydrogen()

        ax = round(mpu6050.accel.x, 2)
        ay = round(mpu6050.accel.y, 2)
        az = round(mpu6050.accel.z, 2)

        gx = round(mpu6050.gyro.x, 2)
        gy = round(mpu6050.gyro.y, 2)
        gz = round(mpu6050.gyro.z, 2)

        f.write(str(t))
        f.write(",")

        f.write(str(Pressure))
        f.write(",")

        f.write(str(temperature))
        f.write(",")

        f.write(str(Smoke))
        f.write(",")

        f.write(str(LPG))
        f.write(",")

        f.write(str(Methane))
        f.write(",")

        f.write(str(Hydrogen))
        f.write(",")

        f.write(str(ax))
        f.write(",")

        f.write(str(ay))
        f.write(",")

        f.write(str(az))
        f.write(",")

        f.write(str(gx))
        f.write(",")

        f.write(str(gy))
        f.write(",")

        f.write(str(gz))
        f.write(",")

        f.write("\n")

        f.flush()

        print("our data saved")
        utime.sleep(1)  # Add a delay to avoid rapid file writing
