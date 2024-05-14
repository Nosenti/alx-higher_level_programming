#!/bin/bash
# Script to display HTTP methods that the server allow
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
