import requests
import sys
from collections import OrderedDict

url = "https://api.macaddress.io/v1"
mac= sys.argv[1]
print(mac)
qs=OrderedDict()
qs = {"apiKey":"at_o45w16Yxa6RDxXNSV7lAZkY4DMax2","output":"json","search":mac}
for key, value in qs.items():
    print(key, value)

response= requests.get(url,params=qs)
print(response.url)
data=response.json()

print(data)
print(f'Vendor oui is: ', data['vendorDetails']['oui'])
print(f'Vendor name is:', data['vendorDetails']['companyName'])