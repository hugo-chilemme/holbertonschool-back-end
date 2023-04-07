#!/usr/bin/python3
"""Importing the request library"""
import requests


def api_request(event_url):
    """ API call function """
    # check that the @event_url is correct
    if event_url is not None and type(event_url) is str:
        
        # Declaration of the REST API url
        url = f"https://jsonplaceholder.typicode.com/{event_url}"

        # Obtaining data
        r = requests.get(url)

        # We check if the request did not fail
        if r.status_code == 200:

            # Returning data in object format
            return r.json()

        # The request failed, the program is stopped
        raise TypeError(f"The URL returned an error {r.status_code}")
