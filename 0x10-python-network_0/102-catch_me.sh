#!/bin/bash
# Script to send a requrest and get a response "You got me"
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

