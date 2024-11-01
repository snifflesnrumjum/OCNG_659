#this is very basic code to measure the distance for
#for the VL53L4CX sensor from adafruit_vl53l4cd
#you will need to copy the adafruit_vl53l4cd package
#to the rp2040 feather board before using this code


import adafruit_vl53l4cd
import board
import time

i2c = board.STEMMA_I2C()

sensor = adafruit_vl53l4cd.VL53L4CD(i2c)

def get_distance():
    sensor.start_ranging()
    time.sleep(0.05)
    sensor.distance
    time.sleep(0.05)
    sensor.stop_ranging()
    sensor.start_ranging()
    time.sleep(0.1)
    sensor.distance
    time.sleep(0.05)
    sensor.stop_ranging()
    return sensor.distance
