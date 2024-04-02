#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)
