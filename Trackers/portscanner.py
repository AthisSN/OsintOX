import socket
import datetime
import sys
from datetime import datetime

def PortScanner():
	host = input("Enter the Target Host: ")
	print("Scanning Target: " + host)
	print("Scanning started at : " + str(datetime.now()))
	try:
		for i in range(1,1024):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result = s.connect_ex((host,i))
			if(result == 0):
				print('Port %d: Open' % (i,))
			s.close()
	except KeyboardInterrupt:
		print("See You Soon")



