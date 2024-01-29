#!/usr/bin/python3
"""defines json"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
alist = list(sys.argv[1:])

try:
    past = load_from_json_file('add_item.json')
except Exception:
    past = []

past.extend(alist)
save_to_json_file(past, 'add_item.json')
