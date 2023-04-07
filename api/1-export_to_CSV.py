#!/usr/bin/python3
"""Script to export user tasks to CSV"""
from api_request import api_request
import sys


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

                # Inserting data line by line
                csv = ""
                for todo in todos:
                    csv += '"{}","{}","{}","{}"\n'.format(
                        todo["userId"],
                        user["username"],
                        todo["completed"],
                        todo["title"])

                # Remove last newline
                csv = csv[:-1]

                # Sending data to a .csv file
                with open("{}.csv".format(id), 'w') as csvfile:
                    csvfile.write(csv)
                    csvfile.close()
