#!/usr/bin/python3
"""Sends a POST request with a letter as a parameter and displays the response"""


import sys
import requests


def search_user(letter):
    """Sends a POST request to search for a user"""
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    search_user(letter)
