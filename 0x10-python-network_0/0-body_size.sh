#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -sI <URL> | awk '/Content-Length/ {print $2}' | tr -d '\r'
