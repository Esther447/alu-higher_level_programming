#!/bin/bash
#This script sends a POST request to the passed URL, and displays the body of the response
curl -s -X post -d "email=e.mushimiyi@alustudent.com&subject=I will always be here for PLD"  "$1"
