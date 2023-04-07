#!/usr/bin/python3
"""script to get all done task of the user"""
from api_request import api_request
import sys


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
