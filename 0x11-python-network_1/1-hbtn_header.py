#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the header
    of the response to a request sent to the given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable found in the response header.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        return x_request_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = fetch_x_request_id(url)
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
