#!/bin/bash
#script that takes in a URL, sends a POST request to the passed URL
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
