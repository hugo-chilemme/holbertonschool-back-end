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
                completed = list(filter(lambda todo: todo["completed"], todos))
                EMPLOYEE_NAME = user['name']
                NUMBER_OF_DONE_TASKS = len(completed)
                TOTAL_NUMBER_OF_TASKS = len(todos)
                print("Employee {} is done with tasks({}/{}):".format(
                    EMPLOYEE_NAME,
                    NUMBER_OF_DONE_TASKS,
                    TOTAL_NUMBER_OF_TASKS
                ))
                for todo in completed:
                    print("\t {}".format(todo['title']))
