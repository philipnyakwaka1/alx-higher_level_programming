#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import sys
from urllib import request
with request.urlopen(sys.argv[1]) as response:
    if response.headers['X-Request-Id'] is not None:
        print(response.headers['X-Request-Id'])
