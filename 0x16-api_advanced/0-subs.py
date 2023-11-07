#!/usr/bin/python3
"""A module that queries the Reddit API"""


import requests


def number_of_subscribers(subreddit):
    """Method that queries the reddit API for total subscribers
    of a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    return 0
