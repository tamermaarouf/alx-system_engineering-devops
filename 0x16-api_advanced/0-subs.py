#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribeson a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16 api advanced v1"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 400:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

