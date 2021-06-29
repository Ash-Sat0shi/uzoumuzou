#!/usr/bin python3
# -*- coding: utf-8 -*-
# before use, do
# sudo apt-get -y install python3-dev
# sudo apt-get -y install python3-pip

import RPi.GPIO as GPIO
import time
import datetime

# for send Gmail
import smtplib
import netifaces as ni
from email.utils import formatdate
# for Japanese content
from email.mime.text import MIMEText

ni.ifaddresses('eth0')
myip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

# Gmail Account Settings
gmail_addr = "leakdetectpi@gmail.com"
gmail_pass = "shinshuleak"
SMTP = "smtp.gmail.com"
PORT = 587

from_addr = gmail_addr	# sender addr
#to_addr = "satoshi.yatabe@shin-shu.co.jp"
to_addr = "satoshi.yatabe@shin-shu.co.jp, tokiwabashi_alert_m@toda.co.jp"
subject1 = "漏水検知システム　2号機 DetectPi2-TOKIWA-BRIDGE"
subject2 = "停電検知システム　2号機 DetectPi2-TOKIWA-BRIDGE"
subject3 = "タンク水位検知システム　2号機 DetectPi2-TOKIWA-BRIDGE"

# -- main --

PIN_IN1 = 24
PIN_IN2 = 23
PIN_IN3 = 21
PIN_OUT = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_IN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_OUT, GPIO.OUT)
counter = 0

try:
    while True:
        time.sleep(1)     # to avoid false positive at the first time python runs
        flag1 = GPIO.input(PIN_IN1) == GPIO.HIGH
        flag2 = GPIO.input(PIN_IN2) == GPIO.HIGH
        flag3 = GPIO.input(PIN_IN3) == GPIO.HIGH
        
        
        

        if flag1 == True:
            counter = counter+1
            with open('log.txt', mode='a') as f:
                f.write('発生時刻:' + str(datetime.datetime.now()) + '漏水を検知 回数：' + str(counter) + '\n')
            print("発生時刻:")
            print(datetime.datetime.now())
            print("WATER DETECTED!! 漏水を検知しました！！ time : {0}".format(datetime.datetime.now))
            body1 = "発生時刻 : {0} \n 漏水を検知しました！！ \n RasPi IP Address is : {1} ".format(datetime.datetime.now(), myip)
            msg1 = MIMEText(body1, "plain", "utf-8")
        # prevent 'ascii' codec can't encode characters in position 0-14: ordinal not in range(128) というエラーがでる
            msg1["From"] = from_addr
            msg1["To"] = to_addr
            msg1["Date"] = formatdate()
            msg1["Subject"] = subject1
            
            time.sleep(5)

            # -------------------------------------------------------------------------------------------------------------
            # send mail
            if counter == 5:
                
                try:
                    GPIO.output(PIN_OUT, flag1)
                    print("sending 漏水 mail...")
                    with open('log.txt', mode='a') as f:
                        f.write('送信時刻:' + str(datetime.datetime.now()) + 'メール送信中…')
                    send = smtplib.SMTP(SMTP, PORT)		# create SMTP object
                    send.ehlo()
                    send.starttls()
                    send.ehlo()
                    send.login(gmail_addr, gmail_pass)	# Login to Gmail
                    send.send_message(msg1)
                    send.close()
                    counter = 0
                    
                except Exception as e:
                    print("except: " + str(e))		# in case of error
                    with open('log.txt', mode='a') as f:
                        f.write('メール送信エラー' + str(e) + '\n')
                else:
                    print("Successfully sent WATER LEAKAGE mail to {0}".format(to_addr))	# when succeed
                    with open('log.txt', mode='a') as f:
                        f.write('……メール送信完了' + '\n')
                    print(body1)
                    time.sleep(10080)
                    GPIO.output(PIN_OUT, 0)
            # -------------------------------------------------------------------------------------------------------------
        elif flag2 == True:
            counter = counter+1
            with open('log.txt', mode='a') as f:
                f.write('発生時刻:' + str(datetime.datetime.now()) + '停電を検知 回数：' + str(counter) + '\n')
            print("発生時刻:")
            print(datetime.datetime.now())
            print(" BLACKOUT DETECTED!! 停電を検知しました！！ time : {0}".format(datetime.datetime.now))
            body2 = "発生時刻 : {0} \n 停電を検知しました！！ \n RasPi IP Address is : {1} ".format(datetime.datetime.now(), myip)
            msg2 = MIMEText(body2, "plain", "utf-8")
        # prevent 'ascii' codec can't encode characters in position 0-14: ordinal not in range(128) というエラーがでる
            msg2["From"] = from_addr
            msg2["To"] = to_addr
            msg2["Date"] = formatdate()
            msg2["Subject"] = subject2
            
            time.sleep(5)
            # -------------------------------------------------------------------------------------------------------------
            # send mail
            if counter == 5:
                try:
                    GPIO.output(PIN_OUT, flag2)
                    print("sending 停電 mail...")
                    with open('log.txt', mode='a') as f:
                        f.write('送信時刻:' + str(datetime.datetime.now()) + 'メール送信中…')
                    send = smtplib.SMTP(SMTP, PORT)		# create SMTP object
                    send.ehlo()
                    send.starttls()
                    send.ehlo()
                    send.login(gmail_addr, gmail_pass)	# Login to Gmail
                    send.send_message(msg2)
                    send.close()
                    counter = 0
                except Exception as e:
                    print("except: " + str(e))		# in case of error
                    with open('log.txt', mode='a') as f:
                        f.write('メール送信エラー' + str(e) + '\n')
                else:
                    print("Successfully sent BLACKOUT mail to {0}".format(to_addr))	# when succeed
                    with open('log.txt', mode='a') as f:
                        f.write('……メール送信完了' + '\n')
                    print(body2)
                    time.sleep(10080)
                    GPIO.output(PIN_OUT, 0)
                # -------------------------------------------------------------------------------------------------------------
        elif flag3 == True:
            counter = counter+1
            with open('log.txt', mode='a') as f:
                f.write('発生時刻:' + str(datetime.datetime.now()) + 'タンク水位上昇を検知 回数：' + str(counter) + '\n')
            print("発生時刻:")
            print(datetime.datetime.now())
            print(" TANK LEVEL RISING DETECTED!! 水位上昇を検知しました！！ time : {0}".format(datetime.datetime.now))
            body3 = "発生時刻 : {0} \n タンク水位上昇を検知しました！！ \n RasPi IP Address is : {1} ".format(datetime.datetime.now(), myip)
            msg3 = MIMEText(body3, "plain", "utf-8")
        # prevent 'ascii' codec can't encode characters in position 0-14: ordinal not in range(128) というエラーがでる
            msg3["From"] = from_addr
            msg3["To"] = to_addr
            msg3["Date"] = formatdate()
            msg3["Subject"] = subject3
            
            time.sleep(5)
            # -------------------------------------------------------------------------------------------------------------
            # send mail
            if counter == 5:
                try:
                    GPIO.output(PIN_OUT, flag3)
                    print("sending 水位上昇 mail...")
                    with open('log.txt', mode='a') as f:
                        f.write('送信時刻:' + str(datetime.datetime.now()) + 'メール送信中…')
                    send = smtplib.SMTP(SMTP, PORT)		# create SMTP object
                    send.ehlo()
                    send.starttls()
                    send.ehlo()
                    send.login(gmail_addr, gmail_pass)	# Login to Gmail
                    send.send_message(msg3)
                    send.close()
                    counter = 0
                except Exception as e:
                    print("except: " + str(e))		# in case of error
                    with open('log.txt', mode='a') as f:
                        f.write('メール送信エラー' + str(e) + '\n')
                else:
                    print("Successfully sent TANK LEVEL RISING mail to {0}".format(to_addr))	# when succeed
                    with open('log.txt', mode='a') as f:
                        f.write('……メール送信完了' + '\n')
                    print(body3)
                    time.sleep(10080)
                    GPIO.output(PIN_OUT, 0)
        else:
            print("ALL GREEN")
            GPIO.output(PIN_OUT, 0)
            time.sleep(4)
            counter = 0
                    
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

# -- main end --
