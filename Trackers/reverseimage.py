import requests
import webbrowser

def ReverseImage():
	try:
		print('')
		path = input("Enter the Image Path to Reverse the image: ")
		url = 'https://www.google.co.in/searchbyimage/upload'
		multipart = {'encoded_image': (path, open(path, 'rb')), 'image_content': ''}
		response = requests.post(url, files=multipart, allow_redirects=False)
		fetchUrl = response.headers['Location']
		webbrowser.open(fetchUrl)

	except FileNotFoundError:
		print("File Not Found")

