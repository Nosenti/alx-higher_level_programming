#!/usr/bin/python3
"""Using urllib to fetch response"""
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
