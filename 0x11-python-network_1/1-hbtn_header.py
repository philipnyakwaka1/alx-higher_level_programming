#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

from urllib import request
import sys
with request.urlopen(sys.argv[1]) as response:
    if response.headers['X-Request-Id'] is not None:
        print(response.headers['X-Request-Id'])
