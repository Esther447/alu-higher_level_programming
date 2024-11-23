#!/usr/bin/python3
"""I documented"""


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
