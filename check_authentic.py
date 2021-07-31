import serial
import time

serialcomm = serial.Serial('COM7', 9600)
serialcomm.timeout = 1

id = "6563226356635"

while True:
	x = serialcomm.readline().decode('ascii')
	if x==id:
		serialcomm.write("Yes".encode())