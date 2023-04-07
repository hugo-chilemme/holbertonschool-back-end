#!/usr/bin/python3
"""Script to export user tasks to JSON file"""
import json
import requests
import sys


def api_request(event_url):
    """ API call function """
    if event_url is not None and type(event_url) is str:
        url = "https://jsonplaceholder.typicode.com/{}".format(event_url)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        raise TypeError("The URL returned an error {}".format(r.status_code))


if __name__ == '__main__':
    """script to get all done task of the user"""

    # User Recovery
    users_list = api_request("users")
    if len(users_list) > 0:

        # Creation of a dictionary to access the user more quickly
        users = {}
        for user in users_list:
            users[user['id']] = user

        # Users task retrievals
        todos = api_request("todos")
        if len(todos) > 0:

            # Creation of the final table
            callback = {}

            # We browse data by data to add in the table
            for todo in todos:
                userId = str(todo['userId'])
                # We check that the user table does not exist to create it
                if userId not in callback:
                    callback[userId] = []

                # Adding the task in the user table
                callback[userId].append({
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": users[int(userId)]['username']
                })
            print(callback)

            # Sending data to a .json file
            with open("todo_all_employees.json", 'w') as csvfile:
                csvfile.write(json.dumps(callback))
                csvfile.close()
