#!/usr/bin/python3
"""
This module parses the title of all hot articles
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if not word_list or word_list == [] or not subreddit:
        return

    session = requests.Session()
    session.timeout = 5

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    header = {"User-Agent": "Reddit hot search (https://github.com/Medjai229)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = session.get(url, headers=header, params=params,
                           allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    after = data["data"]["after"]
    hot_posts = data["data"]["children"]

    for post in hot_posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda kv: (-kv[1], kv[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
