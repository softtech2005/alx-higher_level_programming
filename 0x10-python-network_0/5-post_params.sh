#!/bin/bash
# This script takes in a URL as an argument, sends a POST request with specified parameters, and displays the body of the response

# Send a POST request to the URL with specified parameters and display the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
