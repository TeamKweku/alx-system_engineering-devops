#!/usr/bin/python3
"""A module that queries the Reddit API"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Method that queries the reddit API for hot topics"""
    url = "https://www.reddit.com/r/{}" \
        "/hot.json?after={}".format(subreddit, after)
    headers = {"User-Agent": "Custom/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get("data").get("children")
        for entry in children:
            hot_list.append(entry.get("data").get("title"))

        after = data.get("data").get("after")
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
