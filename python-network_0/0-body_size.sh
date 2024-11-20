#!/bin/bash
# This script sends a request to URL and displays the size of the response i bytes
curl -sI "$1" | grep -i content-length | cut -f2 -d' '
