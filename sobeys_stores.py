import requests
import json
import csv
from key import API_KEY

def get_locations_postalcode(postalcode):
  stores = {}
  pcode = postalcode.upper()


  # get info from google maps API
  gurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
  g_params = {
    'key':API_KEY,
    'address': pcode
  }
  # get JSON
  ginfo = requests.get(gurl, params=g_params).json()

  # parse JSON
  lat = ginfo['results'][0]['geometry']['location']['lat']
  lng = ginfo['results'][0]['geometry']['location']['lng']

 #stores around certain location - gets their external id, which we need for the appointments request
  url = "https://api.pharmacyappointments.ca/public/locations/search"

  payload = json.dumps({
    "location": {
      "lat": lat,
      "lng": lng
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

  return locations

print(get_locations('L1N4J6'))
