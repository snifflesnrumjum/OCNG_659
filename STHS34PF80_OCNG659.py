import board
import busio
import time
from adafruit_bus_device.i2c_device import I2CDevice

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
sensor_address = 0x5A  # Replace with your sensor's I2C address
sensor = I2CDevice(i2c, sensor_address)

def write_register(register, value):
    with sensor:
        sensor.write(bytes([register, value]))

def read_register(register, length):
    buffer = bytearray(length)
    with sensor:
        sensor.write_then_readinto(bytes([register]), buffer)
    return buffer

# Step 1: Enable access to the embedded functions registers
write_register(0x21, 0x01)

# Step 2: Enable write operation
write_register(0x11, 0x01)

# Step 3: Set register address (RESET_ALGO register)
write_register(0x08, 0x2A)

# Step 4: Write register value (set ALGO_ENABLE_RESET bit)
write_register(0x09, 0x01)

# Step 5: Disable write operation
write_register(0x11, 0x00)

# Step 6: Disable access to the embedded functions registers
write_register(0x21, 0x00)

# Step 7: Start acquiring data at the desired ODR value
# Set ODR [3:0] to 0100
odr_value = 0x04
write_register(0x20, odr_value)

# Step 8: Read IR data from the sensor
# Read low and high bytes of the object temperature
tobject_l = read_register(0x26, 1)[0]
tobject_h = read_register(0x27, 1)[0]

# Combine the low and high bytes to get the full object temperature value
tobject = (tobject_h << 8) | tobject_l

# Convert the raw value to a meaningful temperature if needed
# This conversion depends on the sensor's datasheet
print("Object temperature (IR data):", tobject)

def testing(t=100):
    for x in range(t):
        tobject_l = read_register(0x26, 1)[0]
        tobject_h = read_register(0x27, 1)[0]

        tobject = (tobject_h << 8) | tobject_l

        print("Object temperature (IR data):", tobject)
        time.sleep(0.1)

