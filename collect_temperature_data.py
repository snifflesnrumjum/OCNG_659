import time
from adafruit_circuitplayground import cp
import storage

#remount the filesystem to make it writable
storage.remount('/', readonly=False)


def take_reading():
    #set up our file that we will write to
    f = open('oct_18_class.csv', 'a')  #second argument is whether to read (r), write (w) or append (a)

    #collect the temperature and write it to the file
    temperature = cp.temperature
    current_time = time.localtime()
    f.write(str(current_time.tm_hour)+':'+str(current_time.tm_min)+':'+str(current_time.tm_sec))
    f.write(' '+str(temperature)+'\n')
    f.close()
    return

while True:
    take_reading()
    time.sleep(1)

