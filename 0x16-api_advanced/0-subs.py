#!/usr/bin/python3
"""function that queries reddit and returns subscribers"""


import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    a = requests.get(url, headers=headers)
    if a.status_code == 200:
        d = a.json()
        return d['data']['subscribers']
    else:
        return 0
