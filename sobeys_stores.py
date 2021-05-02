import requests
import json
import csv

stores = {}

with open("./canadacities.csv", "r") as file:
  reader = csv.reader(file)
  for row in reader:
    if(row[0]) == 'city':
      continue

    ### stores around certain location - gets their external id, which we need for the appointments request
    url = "https://api.pharmacyappointments.ca/public/locations/search"

    payload = json.dumps({
      "location": {
        "lat": float(row[4]),
        "lng": float(row[5])
      },
      "fromDate": "2021-05-01",
      "vaccineData": "WyJhM3A1bzAwMDAwMDAwVzdBQUkiLCJhM3A1bzAwMDAwMDAwVzJBQUkiLCJhM3A1bzAwMDAwMDAwVzNBQUkiLCJhM3A1bzAwMDAwMDAwVzVBQUkiLCJhM3A1bzAwMDAwMDAwV1dBQVkiLCJhM3A1bzAwMDAwMDAwZjRBQUEiLCJhM3A1bzAwMDAwMDAwZk9BQVEiLCJhM3A1bzAwMDAwMDAwZllBQVEiLCJhM3A1bzAwMDAwMDAwZ2xBQUEiLCJhM3A1bzAwMDAwMDAwbnJBQUEiLCJhM3A1bzAwMDAwMDAwZkpBQVEiXQ==",
      "locationQuery": {
        "includePools": [
          "default"
        ]
      },
      "doseNumber": 1,
      "url": "https://www.pharmacyappointments.ca/location-select"
    })
    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.9',
      'content-length': '537',
      'content-type': 'application/json',
      'origin': 'https://www.pharmacyappointments.ca',
      'referer': 'https://www.pharmacyappointments.ca/',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
      'x-correlation-id': '4d2a6fae-6f0c-4ff0-bca0-58bbd03ec9fb'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    locations = json.loads(response.text)["locations"]

    for location in locations:
      if location["name"] not in stores.keys():
        object = {
          "displayAddress": location["displayAddress"],
          "extId": location["extId"],
          "regionExternalId": location["regionExternalId"],
          "location": location["location"],
          "type": location["type"],
          "timezone": location["timezone"]

        }
        stores[ location["name"] ] = object

with open('sobeys_stores.json', 'w') as f:
    json.dump(stores, f, indent=4)