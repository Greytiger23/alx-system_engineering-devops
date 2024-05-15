#!/usr/bin/python3
"""queries and count words reddit"""


import requests


def count_words(subreddit, word_list, after=None, word_counts={}):
    if after is None:
        word_counts.clear()
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {'User-Agent': 'Custom User Agent'}
        params = {'limit': 100, 'after': after}
        a = requests.get(url, headers=headers, params=params)
        if a.status_code != 200:
            return
        d = response.json()
        b = d['data']['children']
        for post in b:
            title = post['data']['title'].lower()
            for y in word_list:
                if y.lower() in title.split():
                    word_counts[y.lower()] = word_counts.get(
                            y.lower(), 0) + 1
        after = d['data']['after']
        if after:
            return count_words(subreddit, word_list,
                               after, word_counts)
        else:
            sorted_word_counts = sorted(word_counts.items(
                              ), key=lambda x: (-x[1], x[0]))
        for y, count in sorted_word_counts:
            print(f"{y}: {count}")
