#!/usr/bin/python3
"""
This module returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively fetches hot articles from a subreddit
    and returns a list of hot posts titles
    """
    session = requests.Session()
    session.timeout = 5

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    header = {"User-Agent":
              "Reddit Hot posts titles v1.0 (https://github.com/Medjai229)"}
    param = {"after": after, "count": count}
    response = session.get(url, headers=header, params=param,
                           allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    after = data["data"]["after"]
    count += data["data"]["dist"]
    hot_posts = data["data"]["children"]
    for post in hot_posts:
        hot_list.append(post["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
