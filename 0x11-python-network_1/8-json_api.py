#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == '__main__':
    l = sys.argv[1] if len(sys.argv) > 1 else ""
    value = {'q': l}
    response = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        if len(response.json()) == 0:
            print('No result')
        else:
            print(f'[{response.json().get("id")}] {response.json().get("name")}')
    except Exception as e:
        print('Not a valid JSON')
