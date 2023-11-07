#!/usr/bin/python3
"""A module that queries the Reddit API"""


import requests


def top_ten(subreddit):
    """Method that queries the reddit API for top 10 hot topics"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')
        for entry in children:
            print(entry.get('data').get('title'))
    else:
        print(None)
