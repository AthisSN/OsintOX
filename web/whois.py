import whois

def Whois(host,port):
	host = input("Enter the target host: ")
	domain = whois.whois(host)
	print(domain)

