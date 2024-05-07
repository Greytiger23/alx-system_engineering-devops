#!/usr/bin/python3
"""function that queries reddit and returns subscribers"""


import requests


def number_of_subscribers(subreddit):
    """get number of subs"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'request'}
    a = requests.get(url, headers=headers, allow_redirects=False)
    if a.status_code == 200:
        d = response.json()
        x = d['data']['subscribers']
        return x
    else:
        return 0
