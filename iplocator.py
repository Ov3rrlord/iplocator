import json
import sys
from datetime import datetime
import requests
from config import auth

API_KEY = auth.api
print()
IP = input("Please insert the IP address here: ").strip()
print()

try:
    response = requests.get(f'https://api.geoapify.com/v1/ipinfo?ip={IP}&apiKey={API_KEY}')
    data = response.json()

    latitude = data["location"].get("latitude")
    longitude = data["location"].get("longitude")
    dp = data["subdivisions"][0].get("names")

    with open("location.json", "w") as write_file:
        json.dump(data, write_file, indent=4)

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

    print("*" * 48 + "\n")

    # generate google map link
    def google_map(lat, long) -> int:
        if latitude and longitude is None:
            print("No google map link available.")
            sys.exit(1)
        else:
            map_url = f"https://maps.google.com/?q={latitude},{longitude}"
            print("Google map link:", map_url)
            print()


    google_map(lat=latitude, long=longitude)

except KeyError as e:
    print("An error occurred, please try again.")
    sys.exit(1)
