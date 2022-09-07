#!/usr/bin/python3
# coding: utf-8

import requests

resp = requests.post('http://localhost:8000/upload/',
              files={
                  'img': ('code.png', open('code.png', 'rb'), 'image/png')
              })

print(resp.json())
