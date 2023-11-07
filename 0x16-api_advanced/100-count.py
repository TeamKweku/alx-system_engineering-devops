#!/usr/bin/python3
"""A module that queries the Reddit API"""


import requests


def count_words(subreddit, word_list, array=None, after=None):
    """Method that queries the reddit API for hot topics"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get("data").get("children")

        for entry in children:
            splitted = entry.get("data").get("title").lower().split()

            for word in word_list:
                if word.lower() in splitted:
                    count = len([c for c in splitted if c == word.lower()])
                    if array.get(word) is None:
                        array[word] = count
                    else:
                        array[word] += count

        after = data.get("data").get("after")
        if after:
            count_words(subreddit, word_list, array, after)
        else:
            sorted_res = sorted(array.items(), key=lambda x: (-x[1],
                                                              x[0].lower()))

            for word, count in sorted_res:
                print("{}: {}".format(word.lower(), count))
