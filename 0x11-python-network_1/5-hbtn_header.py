#!/usr/bin/python3
"""
Sends a request to URL and displays the value
of the X-Request-Id variable found in the res header.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_requrest_id = response.headers.get('X-Request-Id')
    print(x_requrest_id)
