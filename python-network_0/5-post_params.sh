#!/bin/bash
#This script sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -d "email=e.mushimiyi@gmail.com&subject=I will always be here for PLD" "$1"
