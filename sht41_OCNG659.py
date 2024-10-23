import board
import adafruit_sht4x
from adafruit_bus_device.i2c_device import I2CDevice


i2c = board.STEMMA_I2C()

#create the object that represents the sensor
sht41 = adafruit_sht4x.AHT4x(i2c)

#get the temperature and relative humidity readings
temperature = sht41.temperature
humidity = sht41.relative_humidity
