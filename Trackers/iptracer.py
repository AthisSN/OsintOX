import os
import json
import urllib.request

def IpTracker():
	while True:
		print('')
		ip = input("ENTER THE IP ADDRESS OF THE TARGET SYSTEM: ")
		api = "http://ip-api.com/json/"
		response = urllib.request.urlopen(api + ip)
		data = response.read()
		value = json.loads(data)

		print("IP: " + value['query'])
		print("ISP: " + value['isp'])
		print("Country: " + value['country'])
		print("RegionName: " + value['regionName'])
		print("Region: " + value['region'])
		print("City: " + value['city'])
		print("PinCode: " + value['zip'])
		print("Org: " + value['org'])
		break

