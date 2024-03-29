#!/usr/bin/python3
# Python script that takes in a URL

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.URLError as e:
    print(e.reason)
