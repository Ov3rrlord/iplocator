import sys
import json
import requests

# Check if the IP address is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <IP>")
    sys.exit(1)

# Get the IP address from the command-line argument
IP = sys.argv[1]

response = requests.get(f'http://api.db-ip.com/v2/free/{IP}')
data = response.json()

with open("location.json", "a") as write_file:
    json.dump(data, write_file, indent=4)

print("*"*50)
print("Continent:      ", data.get("continentName"))
print("Country code:   ", data.get("countryCode"))
print("Country:        ", data.get("countryName"))
print("State/Province: ", data.get("stateProv"))
print("City:           ", data.get("city"))
print("*"*50)
