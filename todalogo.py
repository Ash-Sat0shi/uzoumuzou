#!/usr/bin python3
# -*- coding: utf-8 -*-
import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Raspberry Pi pin configuration:
oled_reset = digitalio.DigitalInOut(board.D4)



# 128x32 display with hardware I2C:
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
i2c = board.I2C()
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=xxx)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Load image based on OLED display height.  Note that image is converted to 1 bit color.
image = Image.open('todalogo.ppm').convert('1')
#image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

# Display image.
oled.image(image)
oled.show()
