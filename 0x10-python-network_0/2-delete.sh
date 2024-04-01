#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Send a DELETE request to the URL and display the body of the response
curl -sX DELETE "$1"
