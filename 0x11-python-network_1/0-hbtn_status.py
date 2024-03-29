#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        datas = data.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", datas)
except urllib.error.URLError as e:
    print(e.reason)
