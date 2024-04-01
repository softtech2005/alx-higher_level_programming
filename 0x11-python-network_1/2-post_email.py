#!/usr/bin/python3
"""Sends a POST request with an email as a parameter"""


import sys
import urllib.parse
import urllib.request


def post_email(url, email):
    """Sends a POST request with the given email"""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
