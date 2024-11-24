#!/usr/bin/python3
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    body =  response.text


    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
