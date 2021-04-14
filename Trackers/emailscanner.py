import requests
import json

def EmailScanner():
	email = input("Enter your EmailId: ")
	url = "https://www.troyhunt.com/authentication-and-the-have-i-been-pwned-api/"+email
	print('')
	print("Checking")
	request = requests.get(url,timeout=7)
	status = request.status_code

	if status == 200:
		print("Your Email Has Been Breached")
		data = request.content.decode('utf-8','ignore')
		output = json.loads(data)
		for item in output:
			print('')
			print('\n'
				'[+] Breach      : ' + str(item['Title']) + '\n'
	                  	'[+] Domain      : ' + str(item['Domain']) + '\n'
                  		'[+] Date        : ' + str(item['BreachDate']) + '\n'
                  		'[+] Fabricated  : ' + str(item['IsFabricated']) + '\n'
                  		'[+] Verified    : ' + str(item['IsVerified']) + '\n'
                  		'[+] Retired     : ' + str(item['IsRetired']) + '\n'
                  		'[+] Spam        : ' + str(item['IsSpamList']))

	elif status == 404:
		print("The Email is Not Breached")

	elif status == 503:
		print(" Request Blocked by Cloudflare DDoS Protection")

	elif status == 403:
		print(" Request Blocked by haveibeenpwned API")

	else:
		print(" An Unknown Error Occurred")


