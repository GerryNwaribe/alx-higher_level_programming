#!/usr/bin/python3
"""Python Script"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status'
                                ) as response:
        # Read the response content only once
        response_content = response.read()
        bytes = type(response_content)

        # Decode the content using the charset
        utf8_content = response_content.decode('utf-8')

        print("Body response:")
        print(f"\t- type: {bytes}")  # Since we are dealing with bytes
        print(f"\t- content: {response_content}")
        print(f"\t- utf8 content: {utf8_content}")
