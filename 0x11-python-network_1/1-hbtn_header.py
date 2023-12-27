#!/usr/bin/python3
"""Python script that fetches header https://alx-intranet.hbtn.io/status"""
from urllib import request
import sys
with request.urlopen(sys.argv[1]) as response:
    if response.headers['X-Request-Id'] is not None:
        print(response.headers['X-Request-Id'])
