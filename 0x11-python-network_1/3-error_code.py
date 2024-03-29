#!/usr/bin/python3
# Python script that takes in a URL and an email,
# sends a POST request to the passed URL

import urllib.request
import urllib.error
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
