#!/usr/bin/python3
"""
A script that:
- Takes in a letter
- Sends a POST request to http://0.0.0.0:5000/search
- Displays the id and name from the JSON response if available
"""
import sys
import requests

if __name__ == "__main__":
    # Set the letter to empty string if no argument is given
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    try:
        # Send POST request
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        # Parse JSON response
        response = r.json()

        # Check if JSON is empty
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # If the response body is not valid JSON
        print("Not a valid JSON")
