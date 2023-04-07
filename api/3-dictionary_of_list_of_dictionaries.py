#!/usr/bin/python3
"""script to get all done task of the user"""
import json
import requests
import sys

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com"
    """script to get all done task of the user"""
    user_data = requests.get("{}/users".format(api_url, id))
    if user_data.status_code == 200:
        users = {}
        for user in user_data.json():
            users[user['id']] = user
        todos = requests.get("{}/todos".format(api_url))
        todos = todos.json()
        callback = {}
        for todo in todos:
            userId = todo['userId']
            if userId not in callback:
                callback[userId] = []
            callback[userId].append({
                "task": todo['title'],
                "completed": todo['completed'],
                "username": users[userId]['username']
            })
        with open("todo_all_employees.json", 'w') as csvfile:
            csvfile.write(json.dumps(callback))
            csvfile.close()
