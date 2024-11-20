#!/bin/bash
# sends GET request to the URL and displays the body of the response only if the status code is 200

curl -s "$1" -o /tmp/response_body && curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && cat /tmp/response_body
