#!/usr/bin/python3
import requests
r = requests.get('https://jsonplaceholder.typicode.com/todos')

if r.status_code == 200:
    print(r.json())
