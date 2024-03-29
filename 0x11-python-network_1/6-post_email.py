#!/usr/bin/python3
# Python script that takes in a URL and an email address,
# sends a POST request to the passed URL with the email as a parameter,
# and finally displays the body of the response.

import requests
import sys

if len(sys.argv) < 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

try:
    response = requests.post(url, data={'email': email})
    response.raise_for_status()
    print(response.text)

except requests.RequestException as e:
        print("Error:", e)

