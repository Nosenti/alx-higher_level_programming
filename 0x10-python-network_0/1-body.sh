#!/bin/bash
# Script to send a GET request to URL and display the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
