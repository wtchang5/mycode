#!/usr/bin/python3

import urllib.request, json
import datetime

url = "http://api.open-notify.org/iss-now.json"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print(data['iss_position'])
#print (json.dumps(data, indent=1))


currentDT = datetime.datetime.now()
print (str(currentDT))


