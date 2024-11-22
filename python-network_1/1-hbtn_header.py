#!/usr/bin/python3
"""
This module takes URL as input, sends request to the URL, and displays the val.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command-line argument
    req = urllib.request.Request(url)

    # Send the request and fetch the response
    with urllib.request.urlopen(req) as response:
        # Get the X-Request-Id header value
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)
