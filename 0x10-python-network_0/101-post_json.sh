#!/bin/bash
# Script to send JSON data
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
