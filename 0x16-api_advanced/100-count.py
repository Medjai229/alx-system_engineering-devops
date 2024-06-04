#!/usr/bin/python3
"""
This module parses the title of all hot articles
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    parses the title of all hot articles
    and prints a sorted count of given keywords
    """
    if not instances:
        for word in word_list:
            if word.lower() not in instances:
                instances[word.lower()] = 0

    session = requests.Session()
    session.timeout = 5

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    header = {"User-Agent":
              "Reddit word search (https://github.com/Medjai229)"}
    param = {"after": after, "count": count, "limit": 100}
    response = session.get(url, headers=header, params=param,
                           allow_redirects=False)

    try:
        data = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    after = data["data"]["after"]
    count += data["data"]["dist"]
    hot_posts = data["data"]["children"]
    for post in hot_posts:
        title = post["data"]["title"].lower().split()
        for word in word_list:
            num_of_times = len([t for t in title if t == word.lower()])
            if instances.get(word) is None:
                instances[word] = num_of_times
            else:
                instances[word] += num_of_times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (kv[-1], kv[0]))
        for key, value in instances:
            print(f"{key}: {value}")
    else:
        count_words(subreddit, word_list, instances, after, count)
