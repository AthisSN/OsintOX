import socket
import pyfiglet
from web.subdomain import SubdomainEnum
from web.reverseip import ReverseIP
from web.cms import CMSdetect
from web.nslookup import NsLookup
from web.whois import Whois

banner = pyfiglet.figlet_format("WebOSINT",font="slant")
print(banner)

host = None
port = None
def Connection():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = s.connect_ex((host,port))
	if result == 0:
		return True
	else:
		return False
def Web():
	global host 
	host = input("Enter the Target Host: ")
	global port
	port = int(input("Enter the Target Port: "))
	print('')
	if Connection()==True:
		print("Host is Alive")
	else:
		print("Host is not alive")
		exit()

WEB = {
	1: SubdomainEnum,
	2: ReverseIP,
	3: CMSdetect,
	4: NsLookup,
	5: Whois
}

def MainMenu():
	Option = 1
	while True:
		print('')
		print("1: Subdomain Enumeration ")
		print("2: ReverseIp")
		print("3: CMSDetection")
		print("4: NsLookup")
		print("5: Whois")
		print("6: Exit??")
		print('')
		Option = int(input(">> "))
		if (Option >= 0) and (Option < 6):
			WEB[Option](host,port)
		elif Option == 6:
			print("SEE YOU SOON ")
			exit()
		else:
			print("Please Select an Proper Option")


if __name__ == "__main__":
	Web()
	MainMenu()
