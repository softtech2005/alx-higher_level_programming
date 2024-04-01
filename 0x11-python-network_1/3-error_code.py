#!/usr/bin/python3
"""Displays the body of the response and handles HTTP errors"""


import sys
import urllib.error
import urllib.request


def fetch_url_content(url):
    """Fetches the body of the response and handles HTTP errors"""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_url_content(url)
