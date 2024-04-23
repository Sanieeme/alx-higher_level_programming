#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
<<<<<<< HEAD
curl -sI <URL> | awk '/Content-Length/ {print $2}' | tr -d '\r'
=======
curl -s -I "$1" | grep -i "Content-Length" | awk '{print $2}'
>>>>>>> bbe57c754f40de97d22cfe075453ea40904923ea
