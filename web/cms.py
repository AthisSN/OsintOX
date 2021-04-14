import requests

def CMSdetect(host,port):
	payload = {'key': '1641c3b9f2b1c8676ceaba95d00f7cf2e3531830c5fa9a6cc5e2d922b2ed7165dcce66', 'url': host}
	api = "https://whatcms.org/APIEndpoint/Detect"
	response = requests.get(api,params=payload)
	data = response.json()
	info = data['result']
	if info['code'] == 200:
		print('Detected CMS     : %s' % cms_info['name'])
		print('Detected Version : %s' % cms_info['version'])
		print('Confidence       : %s' % cms_info['confidence'])
	else:
        	print(info['msg'])
        	print('Detected CMS : %s' % info['name'])
        	print('Detected Version : %s' % info['version'])
