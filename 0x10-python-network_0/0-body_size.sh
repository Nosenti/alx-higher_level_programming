#!/bin/bash
# Script to display the size of the body of response ater sending a requrest to URL
curl -s "$1" -o /dev/null -w '%{size_download}\n'