#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Define the GitHub API endpoint for listing commits
    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to the GitHub API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()

        # Iterate through the commits and print the required information
        for commit in commits[:10]:  # Select the first 10 commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        # Print an error message if the request was not successful
        print(
            f"Error: Unable to fetch commits. \
                Status code: {response.status_code}")
