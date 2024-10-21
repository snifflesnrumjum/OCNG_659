##Let's measure some data and log it into a file

import time
from adafruit_circuitplayground import cp
import storage

#remount the filesystem to make it writable
if cp.switch:
    storage.remount('/', readonly=False)

cp.pixels.brightness=0.3

def take_reading():
    cp.pixels.fill((0,0,0))
    cp.pixels[0] = (255,255,255)
    time.sleep(0.1)
    #collect the temperature and write it to the file
    temperature = cp.temperature
    current_time = time.localtime()
    if cp.switch:
        #set up our file that we will write to
        f = open('oct_21_class.csv', 'a')  #second argument is whether to read (r), write (w) or append (a)
        f.write(str(current_time.tm_hour)+':'+str(current_time.tm_min)+':'+str(current_time.tm_sec))
        f.write(' '+str(temperature)+'\n')
        f.close()
    return

while True:
    take_reading()
    cp.pixels[0] = (0,0,0)
    color = int(cp.temperature)
    time.sleep(0.5)
    cp.pixels.fill((color, 255-color, color+color))
    time.sleep(0.5)
    
