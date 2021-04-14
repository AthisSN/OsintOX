import requests
import json

def SubdomainEnum(host,port):
	url = 'https://www.virustotal.com/vtapi/v2/domain/report'
	params = {'apikey' : '1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453','domain':host}
	response = requests.get (url, params=params)
	subdomain = response.json()
	for x in subdomain['domain_siblings']:
		print(x)


