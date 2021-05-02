import requests
import json
import csv
import datetime

### load stores file
with open('sobeys_stores.json') as file:
    stores = json.load(file)

### put the next few calendar days into an array
today = datetime.date.today()
dates = [ (today + datetime.timedelta(days = n)).strftime("%Y-%m-%d") for n in range(14) ]

print(dates)
print(stores.keys())
### appointments per location

for store in stores.keys():
    for date in dates:

        url = "https://api.pharmacyappointments.ca/public/locations/" + stores[store]["extId"] + "/date/" + date + "/slots"

        payload = "{\"vaccineData\":\"WyJhM3A1bzAwMDAwMDAwVzVBQUkiXQ==\",\"url\":\"https://www.pharmacyappointments.ca/appointment-select\"}"
        headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '113',
        'content-type': 'application/json; charset=UTF-8',
        'cookie': '_gid=GA1.2.791932713.1619923458; _ga=GA1.2.634498702.1618536852; _ga_RJPGSHNVCG=GS1.1.1619923457.2.1.1619923705.0',
        'origin': 'https://www.pharmacyappointments.ca',
        'referer': 'https://www.pharmacyappointments.ca/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'x-correlation-id': '4d2a6fae-6f0c-4ff0-bca0-58bbd03ec9fb'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

