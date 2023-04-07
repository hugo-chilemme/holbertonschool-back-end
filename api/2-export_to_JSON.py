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
    if len(sys.argv) > 1:
        id = sys.argv[1]

        # User Recovery
        user = api_request("users/{}".format(id))
        if len(user) > 0:

            # User task retrievals
            todos = api_request("todos?userId={}".format(id))
            if len(todos) > 0:

                # Create from requested userId: []
                callback = {}
                callback[id] = []

                # We browse data by data to add in the table
                for todo in todos:
                    callback[id].append({
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    })

                # Sending data to a .json file
                with open("{}.json".format(id), 'w') as csvfile:
                    csvfile.write(json.dumps(callback))
                    csvfile.close()
