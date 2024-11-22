#!/user/bin/python3
"""Takes a URL, sends a request, and displays ythe X_Request-Id variable from the header."""
import urllib.request
import sys


if __nmae__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)


    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get("X-request-Id)
        print(x_request-id)
