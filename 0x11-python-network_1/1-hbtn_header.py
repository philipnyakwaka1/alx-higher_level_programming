#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request
import sys
url = sys.argv[1]
with request.urlopen(url) as response:
    print(response.headers)
