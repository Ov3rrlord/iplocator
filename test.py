import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.geoapify.com/v1/ipinfo?&apiKey=00134460071f4fe68ba9ccadef35a4b3"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

print(resp.status_code)