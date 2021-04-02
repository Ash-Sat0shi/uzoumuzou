#!/usr/bin python3
# -*- coding: utf-8 -*-
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# 128x32 display with hardware I2C:
WIDTH = 128
HEIGHT = 32
i2c = busio.I2C(SCL, SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
oled.fill(0)
oled.show()

# Load image based on OLED display height.  Note that image is converted to 1 bit color.
#image = Image.open('testlogo.ppm').convert('1')
image = Image.open('testlogo2.ppm').resize((WIDTH, HEIGHT), Image.ANTIALIAS).convert('1')

# Display image.
oled.image(image)
oled.show()
