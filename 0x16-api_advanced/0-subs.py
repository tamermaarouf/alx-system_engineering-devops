#!/usr/bin/python3

"""Module for task 0"""

def number_of_subscribers(subreddit):
    """Return the total number of subscribeson a given subreddit"""
    import requests

    #header={"User-Agent": "linux:0x16 api advanced v1"}

    response = requests.get("https://www.reddit.com/r/{}/about.json"
            .format(subreddit),
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")

