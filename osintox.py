import sys
import os
import socket
import pyfiglet
from Trackers.numberinfo import PhoneNumberTracker
from Trackers.iptracer import IpTracker
from Trackers.maclookup import mactracker
from Trackers.metadataextracter import metadata
from Trackers.reverseimage import ReverseImage
from Trackers.emailscanner import EmailScanner
from Trackers.portscanner import PortScanner

banner = pyfiglet.figlet_format("OsintOX", font = "slant")
print(banner)
print("A PowerFul OSINT Tool\n")
print("Developed By NadarAthis v1.0\n")

OSINT = {
	1: IpTracker,
	2: PhoneNumberTracker,
	3: mactracker,
	4: metadata,
	5: EmailScanner,
	6: ReverseImage,
	7: PortScanner
}

def MainMenu():
	while True:
		Option = 1
		print('')
		print("1: IpAddress Tracker")
		print("2: PhoneNumber Tracker")
		print("3: MacAddress Tracker")
		print("4: MetaData Extracter")
		print("5: EmailScanner")
		print("6: ReverseImage")
		print("7: PortScanner")
		print("8: EXIT??")
		print('')
		Option = int(input(">> "))
		print('')
		if (Option < 8) and (Option >=1):
			OSINT[Option]()
		elif Option == 8:
			exit()
		else:
			print("Please Select An Proper Option!!!")

if __name__ == "__main__":
	MainMenu()
	Main()

