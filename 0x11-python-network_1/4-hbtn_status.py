#!/usr/bin/python3
"""
Sends a request to URL and displays body of the response
decoded in utf-8. It manages HTTPError exceptions and prints the error code.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"\t- type: {type(body).__name__}")
    print(f"\t- content: {body}")
