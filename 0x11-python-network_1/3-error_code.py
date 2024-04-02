#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # Send a request to the URL
        with request.urlopen(url) as response:
            """
            Get the charset from the response headers,
            defaulting to 'utf-8' if not found
            """
            charset = response.headers.get_content_charset(failobj='utf-8')

            # Read and decode the body of the response using the charset
            body = response.read().decode(charset)
            print(body)
    except error.HTTPError as e:
        # Handle HTTP errors
        print("Error code:", e.code)
    except error.URLError as e:
        # Handle URL errors
        print("URL error:", e.reason)
    except TimeoutError:
        # Handle timeout errors
        print("Request timed out")
