#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    utf_content = content.decode('utf-8')
    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {utf_content}')
