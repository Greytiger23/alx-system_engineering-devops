#!/usr/bin/python3
"""qureries and returns subscribers reddit"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after}
    a = requests.get(url, headers=headers, params=params)
    if a.status_code == 200:
        d = response.json()
        x = d['data']['children']
        for post in x:
            hot_list.append(post['data']['title'])
            after = d['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
