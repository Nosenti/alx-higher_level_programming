#!/usr/bin/python3
"""Using urllib to fetch response
script to take URL, sned s a request and display the value of
X-Request_Id variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
