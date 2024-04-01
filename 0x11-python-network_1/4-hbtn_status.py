#!/usr/bin/python3
"""Fetches the status of a URL using requests"""


import requests


def fetch_url_status(url):
    """Fetches the status of the given URL"""
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url_status(url)
