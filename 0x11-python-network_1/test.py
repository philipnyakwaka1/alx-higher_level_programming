#!/usr/bin/python3
import requests
response = requests.get('https://imgs.xkcd.com/comics/a-minus-minus.png')
with open('comic.png', 'wb') as f:
    f.write(response.content)
