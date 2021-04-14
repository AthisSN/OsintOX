import requests
from requests import get

def NsLookup(host,port):
	data = get('http://api.hackertarget.com/dnslookup/?q=' + host).text
	print(data)
