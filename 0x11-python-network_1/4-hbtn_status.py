#!/usr/bin/python3
# Python script that fetches

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
else:
    print(url)
