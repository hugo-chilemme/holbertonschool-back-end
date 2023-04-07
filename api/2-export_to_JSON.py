#!/usr/bin/python3
"""script to get all done task of the user"""
import json
import requests
import sys

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com"
    """script to get all done task of the user"""
    if len(sys.argv) > 1:
        id = sys.argv[1]
        user = requests.get("{}/users/{}".format(api_url, id))
        if user.status_code == 200:
            user = user.json()
            if len(user) > 0:
                todos = requests.get("{}/todos?userId={}".format(api_url, id))
                todos = todos.json()
                callback = {}
                callback[id] = []
                for todo in todos:
                    callback[id].append({
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    })
                with open("{}.json".format(id), 'w') as csvfile:
                    csvfile.write(json.dumps(callback))
                    csvfile.close()
