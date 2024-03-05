import json
import sys
from datetime import datetime
import requests

# Check if the IP address is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python iplocator.py <IP>")
    sys.exit(1)

# Get the IP address from the command-line argument
IP = sys.argv[1]

response = requests.get(f'https://ipapi.co/{IP}/json/')
data = response.json()

latitude = data.get("latitude")
longitude = data.get("longitude")

with open("location.json", "a") as write_file:
    json.dump(data, write_file, indent=4)

dt = datetime.now()
print("*" * 40)
print("Date and time is: ", dt.strftime("%Y-%m-%d %H:%M:%S"))
print("*" * 40)

print("IP              *", data.get("ip"))
print("Network:        *", data.get("network"))
print("Network version *", data.get("version"))
print("Country code:   *", data.get("country_code"))
print("Country:        *", data.get("country_name"))
print("Region:         *", data.get("region"))
print("City:           *", data.get("city"))
print("Latitude:       *", data.get("latitude"))
print("Longitude:      *", data.get("longitude"))
print("Phone code:     *", data.get("country_calling_code"))
print("Organisation:   *", data.get("org"))
print("Currency:       *", data.get("currency"))
print("Currency name:  *", data.get("currency_name"))
print("Continent Code  *", data.get("continent_code"))

print("*" * 40)
print()


# adding google map links support
def google_map(latitude, longitude):
    if latitude or longitude is None:
        print("No google map link available.")
        sys.exit(1)
    else:
        map_url = f"https://maps.google.com/?q={latitude},{longitude}"
        print("Google map link:", map_url)
        print()


google_map(latitude, longitude)
