import json
import sys
from datetime import datetime
import requests
from config import auth, auth2

API_KEY = auth.api
API_KEY2 = auth2.ipinfoapi
print()
IP = sys.argv[1]
print()

try:
    response = requests.get(f'https://api.geoapify.com/v1/ipinfo?ip={IP}&apiKey={API_KEY}')
    data = response.json()
    response2 = requests.get(f'https://ipinfo.io/{IP}?token={API_KEY2}')
    data2 = response2.json()

    latitude = data["location"].get("latitude")
    longitude = data["location"].get("longitude")
    dp = data["subdivisions"][0].get("names")

    location2 = data2.get("loc")
    location2 = location2.split(',')
    lat2 = location2[0]
    long2 = location2[1]

    with open("location.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
        json.dump(data2, write_file, indent=4)

    dt = datetime.now()
    print("*" * 48)
    print("Date and time is: ", dt.strftime("%Y-%m-%d %H:%M:%S"))
    print("*" * 48)

    print("IP              *", data.get("ip"))
    print("Country code:   *", data["country"].get("iso_code"))
    print("Country:        *", data["country"]["names"].get("en"))
    print("City:           *", data["city"].get("name"))
    print("Department:     *", dp["en"])
    print("Latitude:       *", data["location"].get("latitude"))
    print("Longitude:      *", data["location"].get("longitude"))
    print("Phone code:     *", data["country"].get("phone_code"))
    print("Currency:       *", data["country"].get("currency"))
    print("Continent name: *", data["continent"]["names"].get("en"))
    print("Continent Code  *", data["continent"].get("code"))
    print("Flag:           *", data["country"].get("flag"))
    print("Organisation:   *", data2.get("org"))
    print("Timezone:       *", data2.get("timezone"))

    print("*" * 48 + "\n")

    # generate google map link
    def google_map(lat, long):
        if latitude and longitude is None:
            print("No google map link available.")
            sys.exit(1)
        else:
            # There are two google maps url available because of no accuracy
            map_url = f"https://maps.google.com/?q={lat2},{long2}"
            print("Google map link:", map_url)
            map_url2 = f"https://maps.google.com/?q={latitude},{longitude}"
            print("Second Google map link:", map_url2)


            print()


    google_map(lat=latitude, long=longitude)

except KeyError as e:
    print("An error occurred, please try again.")
    sys.exit(1)
