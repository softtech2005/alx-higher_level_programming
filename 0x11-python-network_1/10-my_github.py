#!/usr/bin/python3
"""Displays the user id using the GitHub API"""


import sys
import requests
from requests.auth import HTTPBasicAuth


def get_github_user_id(username, token):
    """Fetches the user id from GitHub"""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print(None)


if __name__ == "__main__":
    username = "softtech2005"
    token = "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"
    get_github_user_id(username, token)
