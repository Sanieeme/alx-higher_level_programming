#!/usr/bin/python3
# Python script that takes in a URL and an email,
# sends a POST request to the passed URL

import urllib.request
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

r = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(r) as response:
    body = response.read().decode('utf-8')
    print(body)
