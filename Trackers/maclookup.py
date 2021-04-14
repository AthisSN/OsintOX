import requests
from src.api import macvendor

def mactracker():
    mac = input("Enter the MacAddress: ")
    url = "https://api.macvendors.com/v1/lookup/" + mac
    api = "Bearer "+macvendor()
    response = requests.get(url,headers={"Authorization":api})
    result = response.json()
    print('')
    if response.status_code == 200:
        final = result['data']
        print("Manufacturer : " + final['organization_name'])
        print("Manufacturer Address : " + final['organization_address'])
    elif response.status_code == 404:
        print("Error 404 : Mac Address Not found")
    else:
        print("Unexpected Error")
        pass


