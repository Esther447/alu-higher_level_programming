#!/usr/bin/python3
"""
This module takes a URL as an argument, sends a request to the URL, and displays the body of  the response (decoded in UTF-8).

If an HTTP error occurs, it prints 'Error code:' followed by the HTTP status code.
"""


import sys
import urllib.request
impoort urllib.error


if __main__ == "__main__":
    url = sys.argv[1]
    

    try:
        #send the request and display the response body
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
       #Handle HTTPError and print the error code
       print(f"Error code: {e.code}"
