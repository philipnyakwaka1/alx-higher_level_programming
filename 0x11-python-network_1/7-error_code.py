#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""

import sys
import requests

if __name__ == '__main__':
    response = requests.post(sys.argv[1])
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
    print(response.text)
