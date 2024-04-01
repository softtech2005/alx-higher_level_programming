#!/usr/bin/python3
"""Fetches the status of a URL"""


import sys
import urllib.request


def fetch_url_status(url):
    """Fetches the status of the given URL"""
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-hbtn_status.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_url_status(url)
