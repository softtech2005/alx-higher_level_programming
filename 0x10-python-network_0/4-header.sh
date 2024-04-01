#!/bin/bash
# This script takes in a URL as an argument, sends a GET request with a custom header, and displays the body of the response

# Send a GET request to the URL with a custom header and display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
