#!/usr/bin/python3
"""
Sends a request to URL and displays the body of response. If the HTTP
status code is >= 400, prints the error code message.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
