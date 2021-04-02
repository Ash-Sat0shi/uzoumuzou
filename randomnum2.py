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

# CONNECT BUTTON TO PIN4,PIN7!!!!!!
PIN_IN1 = 4

fontsize = 36
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

########################ランダムな 1桁の整数を生成#######################
def random_digits():
    return randint(0,9)

def main():
    try:
        count = 0
        while True:
            time.sleep(0.05)     # to avoid false positive at the first time python runs
            flag1 = GPIO.input(PIN_IN1) == GPIO.HIGH
            
            #value1 = str(random_digits())
            #value2 = str(random_digits())
            #value3 = str(random_digits())
            #value4 = str(random_digits())
            #value5 = str(random_digits())
            #value6 = str(random_digits())
            #value7 = str(random_digits())
            #value8 = str(random_digits())
################上記を下3行でまとめ#########################
            value = [''] * 8
            for i in range (8):
                value[i] = str(random_digits())
            #print(value)
            #8桁の配列として出てくる
            value = value[0] + value[1] + value[2] + value[3] + value[4] + value[5] + value[6] + value[7]
            #8桁のstrとして出てくる
            
            #Image.new(mode("1"means black and white),size,color=0)
            image = Image.new("1", (128, 32))
            draw = ImageDraw.Draw(image)
            # Load default font.
            font = ImageFont.truetype("neon_pixel.ttf",fontsize)
            draw.text((2,5), value, font=font, fill=255)
            # Display image.
            disp.image(image)
            disp.show()
            
        
            if flag1 == True:
                ########################ボタンが押されたら…#######################
                #1文字9ドット幅だよ
                count = count + 1
                value[count] = str(random_digits())

            else:
                pass
            ########################ボタンが押されていないとき#######################
    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
