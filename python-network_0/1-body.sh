#!/bin/bash
# sends GET request to the URL and displays the body of the response only if the status code is 200
curl  -sL "$1"
