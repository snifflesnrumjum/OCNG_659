# this code written for the TAMU OCNG 659 classmethod

# you will need to make sure you copy the adafruit_as7341.mpy file to the lib folder on the
# RP2040 Feather board before using this code
# NOTE: two things need to be copied over to the feather board's lib folder
# Copy the adafruit_register folder over into the lib folder as well as the adafruit_as7341.mpy file
import board
import adafruit_as7341

###########
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
as7341 = adafruit_as7341.AS7341(i2c)

all_light_values = as7341.all_channels

#can call each channel individually
single_channel = as7341.channel_480nm
# change the channel name to one of the following:
# channel_415nm
# channel_445nm
# channel_480nm
# channel_515nm
# channel_555nm
# channel_590nm
# channel_630nm
# channel_680nm
# channel_nir
# channel_clear
