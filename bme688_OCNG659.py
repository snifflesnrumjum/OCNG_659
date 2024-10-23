# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

#this code modified from the source file provided by Adafruit Industries (info shown above)
# you will need to make sure you copy the adafruit_bme680.mpy file to the lib folder on the
# RP2040 Feather board before using this code

import board
import adafruit_bme680

###########
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
bme688 = adafruit_bme680.BME680_I2C(i2c)

temperature = bme688.temperature
humidity = bme688.relative_humidity
pressure = bme688.pressure
altitude = bme688.altitude
gas = bme688.gas
