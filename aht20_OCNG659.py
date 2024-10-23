# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

#this code modified from the source file provided by Adafruit Industries (info shown above)

# you will need to make sure you copy the adafruit_ahtx0.mpy file to the lib folder on the
# RP2040 Feather board before using this code

import board
import adafruit_ahtx0

###########
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
aht20 = adafruit_ahtx0.AHTx0(i2c)

temperature = aht20.temperature
humidity = aht20.relative_humidity

