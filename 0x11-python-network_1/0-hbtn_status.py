#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print(response.headers)
