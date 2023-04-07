#!/usr/bin/python3
"""script to get all done task of the user"""
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
    """ script to get all done task of the user """
    if len(sys.argv) > 1:
        id = sys.argv[1]

        # User Recovery
        user = api_request("users/{}".format(id))
        if len(user) > 0:

            # User task retrievals
            todos = api_request("todos?userId={}".format(id))
            if len(todos) > 0:

                # Recovery of uncompleted tasks
                tasks_not_done = list(
                    filter(lambda todo: todo["completed"], todos)
                )

                # Display Data Initialization
                EMPLOYEE_NAME = user['name']
                NUMBER_OF_DONE_TASKS = len(tasks_not_done)
                TOTAL_NUMBER_OF_TASKS = len(todos)

                # Viewing the user's to-do report
                print("Employee {} is done with tasks({}/{}):".format(
                    EMPLOYEE_NAME,
                    NUMBER_OF_DONE_TASKS,
                    TOTAL_NUMBER_OF_TASKS
                ))

                # Displaying the title of each task
                for todo in tasks_not_done:
                    print("\t {}".format(todo['title']))
