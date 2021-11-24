#!/usr/bin/env python3
import datetime
import time
import serial
import sys

if __name__ == "__main__":
	ser = serial.Serial()
	ser.port = '/dev/ttyS0'
	ser.baudrate = 9600
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	ser.timeout = 1

try:
	ser.close()
	ser.open()
	print("open " + ser.port )
except:
	print("cannot open " + ser.port )
	sys.exit(0)


try:
	while True:
		try:
			#print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
			#s = ser.read(10000).decode('utf-8')
			#s = ser.read(10).decode('utf-8').replace( '\r\n', '' )
			dt_now = datetime.datetime.now()
			time = ser.readline().decode('utf-8').replace( 'Time:', dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
			s = ser.readline().decode('utf-8') 
			if time != "":
				print(time)
			if s != "":
				print(s)
			else:
				pass
		except Exception as e:
			print(e)
except Exception as error:
	print(error)
	pass


finally:
	ser.close()
	print("serial connection closed")
