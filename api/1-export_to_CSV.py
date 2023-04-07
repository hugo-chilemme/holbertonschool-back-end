#!/usr/bin/python3
"""script to get all done task of the user"""
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
                csv = ""
                for todo in todos:
                    csv += '"{}", "{}", "{}", "{}"\n'.format(
                        todo["userId"],
                        user["username"],
                        todo["completed"],
                        todo["title"]
                    )
                csv = csv[:-1]
                with open("{}.csv".format(id), 'w') as csvfile:
                    csvfile.write(csv)
                    csvfile.close()
