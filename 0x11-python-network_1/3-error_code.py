#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request
from urllib.error import URLError, HTTPError

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print(f'Reason: {e.reason}')
    except HTTPError as e:
        print(f'Error code: {e.code}')
