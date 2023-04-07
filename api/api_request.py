import requests

def api_request(event_url):
    """ API call function """
    if event_url is not None and type(event_url) is str:
        url = "https://jsonplaceholder.typicode.com/{}".format(event_url)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        raise TypeError("The URL returned an error {}".format(r.status_code))
