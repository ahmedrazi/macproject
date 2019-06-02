# macproject
By a given MAC address, retrieve OUI vendor information, detect virtual machines, possible applications, read the information encoded in the MAC, and get our research's results regarding the MAC address or the OUI.Find vendor information and other attributes from mac address 
I developed a python script which uses python request libary to send a request along with three parameters 
- APIKey:personal API key can be requested to macaddress.io 
- output: I used json as it gives me a dictionary which helped me to query the various keys 
  'json' — Full MAC address information in JSON format.
  'xml' — Full MAC address information in XML format.
  'csv' — Full MAC address information in CSV format.
  'vendor' (default) — Output vendor company name only, in text format
- search: MAC address or OUI, passed as command line parameter

Example:
Razis-MBP:macadd rahmed$ python3  ~/python-project/web2.py 44:38:39:ff:ef:57
44:38:39:ff:ef:57
apiKey at_o45w16Yxa6RDxXNSV7lAZkY4DMax2
output json
search 44:38:39:ff:ef:57
https://api.macaddress.io/v1?apiKey=at_o45w16Yxa6RDxXNSV7lAZkY4DMax2&output=json&search=44%3A38%3A39%3Aff%3Aef%3A57
{'vendorDetails': {'oui': '443839', 'isPrivate': False, 'companyName': 'Cumulus Networks, Inc', 'companyAddress': '650 Castro Street, suite 120-245 Mountain View  CA  94041 US', 'countryCode': 'US'}, 'blockDetails': {'blockFound': True, 'borderLeft': '443839000000', 'borderRight': '443839FFFFFF', 'blockSize': 16777216, 'assignmentBlockSize': 'MA-L', 'dateCreated': '2012-04-08', 'dateUpdated': '2015-09-27'}, 'macAddressDetails': {'searchTerm': '44:38:39:ff:ef:57', 'isValid': True, 'virtualMachine': 'Not detected', 'applications': ['Multi-Chassis Link Aggregation (Cumulus Linux)'], 'transmissionType': 'unicast', 'administrationType': 'UAA', 'wiresharkNotes': 'No details', 'comment': ''}}
Vendor oui is:  443839
Vendor name is: Cumulus Networks, Inc
