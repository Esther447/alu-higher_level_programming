#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status using urllib.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {}".format(type(body)))
        print(f"\t- content: {}".format(body))
        print(f"\t- utf8 content: {}".format(body.decode("utf-8")))
