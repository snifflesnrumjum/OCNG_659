#base code here was generated using Microsoft Copilot to connect an I2C device
#edited to fix minor errors and add in the conversion
#of values to distance
#
#This code generated as part of the OCNG 659 class at Texas A&M University
#Darren Henrichs - TAMU Oceanography

import board
import time
import busio
from adafruit_bus_device.i2c_device import I2CDevice

class QwiicUltrasonic:
    def __init__(self, i2c, address=0x2F):
        self.i2c_device = I2CDevice(i2c, address)
        self.address = address

    def is_connected(self):
        try:
            with self.i2c_device:
                return True
        except:
            return False

    def trigger_and_read(self):
        with self.i2c_device as i2c:
            i2c.write(bytes([0x01]))
            time.sleep(0.1)
            result = bytearray(2)
            i2c.readinto(result)
            print(result)
            converted = int.from_bytes(result, 'big')
            distance = (converted << 8) | converted
            return distance

    def change_address(self, new_address):
        if new_address < 0x08 or new_address > 0x77:
            raise ValueError("Address out of range")
        with self.i2c_device as i2c:
            i2c.write(bytes([0x80 | new_address]))
        self.address = new_address

    def convert_to_distance(self, value):
        #measured manually using data at bottom of this script and calculated the regression line
        distance = 0.000369*value + 0.041
        return distance

i2c = busio.I2C(board.SCL, board.SDA)
ultrasonic = QwiicUltrasonic(i2c)

if ultrasonic.is_connected():
    print('Sensor connected!')
    while True:
        try:
            distance = ultrasonic.trigger_and_read()
            print('Distance: ', distance, ultrasonic.convert_to_distance(distance), 'cm')
        except RuntimeError:
            print('Retrying...')
        time.sleep(0.1)

else:
    print('Sensor not connected!')
##here are some roughly measured values for the sensor
##these were used to calculate a regression line equation to convert the values into distance
##6682 is 2cm away
##8738 is ~ 3.5cm away
##11822 is ~5cm away
##26214 is ~10 cm away
##42662 is ~15cm away
##52685 is ~20cm away
##16191 is ~6cm
##22102 is ~8cm
##8224 is ~3cm

