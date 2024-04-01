#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable in the response header using requests"""


import sys
import requests


def fetch_request_id(url):
    """Fetches the value of the X-Request-Id variable"""
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_request_id(url)
