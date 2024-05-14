#!/bin/bash
# Script to send a GET request to URL and display the body of a 200 status code response
curl -sLw "%{http_code}" "$1" -o /dev/null | grep -q 200 && curl -s "$1"
