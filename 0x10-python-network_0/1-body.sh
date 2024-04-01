#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Send a GET request to the URL and save the response body to a temporary file
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
