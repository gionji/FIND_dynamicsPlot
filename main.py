import requests

STARTIT_DB_URL = 'https://servicesv2.fleet2track.com/api/PLC/get'

STARTIT_REQUEST_BODY = {
"machineryIds": ["gelli-belloi_01"],
"startDate": "17/01/2020 14:00",
"endDate": "17/01/2020 14:40"
}


url = STARTIT_DB_URL
myobj = STARTIT_REQUEST_BODY

x = requests.post(url, data = myobj)

print(x.text)
