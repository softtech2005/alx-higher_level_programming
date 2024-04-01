#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept

# Send an OPTIONS request to the URL and display the allowed methods
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
