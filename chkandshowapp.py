#!/usr/bin python3
# -*- coding: utf-8 -*-

#引数にSystemctlのステータスを表示したいものを入れると返してくれる

import subprocess
from subprocess import PIPE
import time
import sys
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO
args = sys.argv

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
fontsize = 32
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
        #################### メイン処理 ####################
        while True:
            proc = subprocess.run("sudo systemctl status " + args[1], shell=True, stdout=PIPE, stderr=PIPE, text=True)
            status = proc.stdout
            #print(status)
            l = status.splitlines()[4]
            print("Status of " + args[1] + ": "+ l[11:])
            #print('STDOUT: {}'.format(status))
            
            frame()
            draw.text((3,3), l[11:18], font=font, fill=255)
            oled.image(image)
            oled.show()
            time.sleep(5)
            
            oled.fill(0)
            frame()
            oled.image(image)
            oled.show()
            time.sleep(0.2)
        
        
    except KeyboardInterrupt:
        pass
    finally:
        pass
if __name__ == '__main__':
    main()
        