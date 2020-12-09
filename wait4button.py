#!/usr/bin python3
# -*- coding: utf-8 -*-
# before use, do
# sudo apt-get -y install python3-dev
# sudo apt-get -y install python3-pip

import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import RPi.GPIO as GPIO

# generate random integer values
from random import randint


# Create I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class. (x size, y size, i2c)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

PIN_IN1 = 4
fontsize = 36
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

########################ランダムな n桁の整数を生成#######################
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def main():

    try:
        while True:
            time.sleep(0.05)     # to avoid false positive at the first time python runs
            flag1 = GPIO.input(PIN_IN1) == GPIO.HIGH
        
            if flag1 == True:
                ########################ボタンが押されたら…#######################
                value = str(random_with_N_digits(8))
                image = Image.new("1", (128, 32))
                draw = ImageDraw.Draw(image)
                # Load default font.
                font = ImageFont.truetype("neon_pixel.ttf",fontsize)
                draw.text((2,5), value, font=font, fill=255)
                # Display image.
                disp.image(image)
                disp.show()
            
            else:
            ########################ボタンが押されていないとき#######################
                disp.fill(0)
                disp.show()
    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()