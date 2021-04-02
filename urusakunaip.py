#!/usr/bin python3
# -*- coding: utf-8 -*-
#pip3 install adafruit-circuitpython-ssd1306
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO

import netifaces as ni
ni.ifaddresses('eth0')
myip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# Create I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class. (x size, y size, i2c)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

WIDTH = 128
HEIGHT = 32
#HEIGHT = 64
BORDER = 1

# Clear display.
oled.fill(0)
oled.show()

# Load default font.
fontsize = 24
font = ImageFont.truetype("neon_pixel.ttf",fontsize)
# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
# Draw a white frame
def frame():
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
    draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), outline=0, fill=0,)
    
def main():
    try:
        while True:
                frame()
                draw.text(
                (3, 5),
                myip,
                font=font,
                fill=255,)
                # Display image
                oled.image(image)
                oled.show()
                time.sleep(0.4)
                
                oled.fill(0)
                frame()
                oled.image(image)
                oled.show()
                time.sleep(0.1)
        
    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
if __name__ == '__main__':
    main()