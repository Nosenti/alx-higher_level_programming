#!/usr/bin/python3
"""Using urllib to fetch response
script to take URL, sned s a request and display the value of
X-Request_Id variable found in the header
"""
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
