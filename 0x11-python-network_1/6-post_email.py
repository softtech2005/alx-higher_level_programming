#!/usr/bin/python3
"""Sends a POST request with an email as a parameter using requests"""


import sys
import requests


def post_email(url, email):
    """Sends a POST request with the given email"""
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
