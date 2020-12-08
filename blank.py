#!/usr/bin python3
# -*- coding: utf-8 -*-
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class. (x size, y size, i2c)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


while True:
    # Clear display.
    disp.fill(0)
    disp.show()
    
    time.sleep (1)
    
    disp.fill(1)
    disp.show()
    
    time.sleep (1)