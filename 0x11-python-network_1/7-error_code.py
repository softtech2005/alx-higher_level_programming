#!/usr/bin/python3
"""Displays the body of the response and handles HTTP errors using requests"""


import sys
import requests


def fetch_url_content(url):
    """Fetches the body of the response and handles HTTP errors"""
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_url_content(url)
