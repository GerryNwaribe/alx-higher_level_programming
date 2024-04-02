#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    # Get username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the GitHub API endpoint for user information
    api_url = "https://api.github.com/user"

    # Send a GET request to the GitHub API endpoint with Basic Authentication
    response = requests.get(api_url, auth=(username, password))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()

        # Display the user id
        print("User ID:", user_data['id'])
    else:
        # Print an error message if the request was not successful
        print("Error: Unable to fetch user information. Status code:",
              response.status_code)
