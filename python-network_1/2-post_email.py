#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email parameter
"""
import sys
import urllib.request
import urllib.parse


def post_email():
    url = sys.argv[1]
    email = sys.argv[2]


    data = {'email': email}


    encoded_data = urllib.parse.urlencode(data).encode('utf-8')


    with urllib.request.urlopen(url, encoded_data) as response:
        body = response.read().decode('utf-8)


    print("Your email is: {}".format(email))
    print(body)


if __name__ == "__main__":
    post_email(
