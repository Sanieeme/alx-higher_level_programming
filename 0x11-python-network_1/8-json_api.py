#!/usr/bin/python3
import requests
import sys

url = 'http://0.0.0.0:5000/search_user'

if len(sys.argv) > 1:
    lr = sys.argv[1]
else:
    lr = ""

response = requests.post(url, data={'q': lr})

try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response['id'], json_response['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
