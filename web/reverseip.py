from requests import get
def ReverseIP(host,port):
	api = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
	try:
		result = get(api).text
		print(result)

	except:
		print("Enter a Valid IpAddress")


