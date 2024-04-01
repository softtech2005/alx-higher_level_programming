#!/usr/bin/python3
"""Fetches the last 10 commits of a repository by a specified user using the GitHub API"""


import sys
import requests
from requests.auth import HTTPBasicAuth


def fetch_commits(repo, owner):
    """Fetches the last 10 commits of the repository by the owner"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params, auth=HTTPBasicAuth("", ""))
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)
    
    repo = sys.argv[1]
    owner = sys.argv[2]
    fetch_commits(repo, owner)
