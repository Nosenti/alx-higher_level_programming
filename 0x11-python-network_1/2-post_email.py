#!/usr/bin/python3
"""
Sends a Post request to URL with an email as a parameter
and displays the body
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
