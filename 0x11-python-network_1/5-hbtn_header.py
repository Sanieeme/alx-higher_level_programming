#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
# and displays the value of the variable X-Request-Id in the response header

import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]
try:
    response = requests.get(url)

# Check if X-Request-Id is present in the response headers
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
    else:
        print("X-Request-Id not found in the response headers.")

except requests.RequestException as e:
    print("Error:", e)
