#!/usr/bin/python3
"""
A script that:
- Takes your GitHub credentials (username and personal access token).
- Uses the GitHub API to display your user id.
"""
import sys
import requests

if __name__ == "__main__":
    # GitHub username and personal access token passed as arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for the authenticated user's details
    url = "https://api.github.com/user"

    # Use Basic Authentication with username and token
    response = requests.get(url, auth=(username, token))

    # Parse response
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
