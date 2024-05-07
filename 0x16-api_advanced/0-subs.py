#!/usr/bin/python3
"""function that queries reddit and returns subscribers"""


import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'request'}
    a = requests.get(url, headers=headers, allow_redirects=False)
    if a.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
