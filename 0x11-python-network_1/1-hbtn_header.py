#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable in the response header"""


import sys
import urllib.request


def fetch_request_id(url):
    """Fetches the value of the X-Request-Id variable"""
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_request_id(url)
