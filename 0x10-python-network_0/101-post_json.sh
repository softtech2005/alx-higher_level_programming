 #!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# using the contents of a file passed as the second argument, and displays the body of the response

# Send a POST request with the contents of the JSON file in the body and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
