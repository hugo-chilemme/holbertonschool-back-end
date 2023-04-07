#!/usr/bin/python3
"""Importing the request library"""
import requests
from urllib.parse import urlencode

def api_request(event_url, params = {}):
    """ 
        description:
            API call function 
        parameters:
            @event_url: contains the target route with possibly parameters
            @queries: 
    """
    
    # check that the @event_url is correct
    if event_url is None or type(event_url) is not str:
        
        # The request failed, the program is stopped
        raise TypeError(f"The data is missing or incorrect")
    
    # We check if params is valid
    if params is not None and type(params) is dict:
        
        # transformation of the dictionary into a string "?userId=3&..."
        params = "?" + urlencode(params)
    
    # Declaration of the REST API url
    url = f"https://jsonplaceholder.typicode.com/{event_url}{params}"

    # Obtaining data
    r = requests.get(url)

    # We check if the request did not fail
    if r.status_code == 200:

        try:
            # Returning data in object format
            return r.json()
        
        except :
            
            # We don't return anything, because it's a rest api, it's json.
            return {}

    # The request failed, the program is stopped
    raise TypeError(f"The URL returned an error {r.status_code}")
    
