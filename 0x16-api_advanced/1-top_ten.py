#!/usr/bin/python3
"""queries and returns subscribers reddit"""


import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 10}
    a = requests.get(url, headers=headers, params=params)
    if a.status_code == 200:
        d = response.json()
        for x in d['data']['children']:
            print(x['data']['title'])
    else:
        print(None)
