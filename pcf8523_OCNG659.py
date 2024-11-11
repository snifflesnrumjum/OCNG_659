# this code modified from the Adafruit website:
# https://learn.adafruit.com/adafruit-pcf8523-real-time-clock/rtc-with-circuitpython
# for use in the OCNG659 class

import busio
from adafruit_pcf8523 import pcf8523
import time
import board

#myI2C = busio.I2C(board.SCL, board.SDA)
i2c = board.STEMMA_I2C()
rtc = pcf8523.PCF8523(i2c)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2024,  11,   11,   8,  48,  5,    1,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

    print("Setting time to:", t)     # uncomment for debugging
    rtc.datetime = t
    print()

while True:
    t = rtc.datetime
    #print(t)     # uncomment for debugging

    print("The date is %s %d/%d/%d" % (days[t.tm_wday], t.tm_mday, t.tm_mon, t.tm_year))
    print("The time is %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))

    time.sleep(1) # wait a second
