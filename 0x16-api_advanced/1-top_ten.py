#!/usr/bin/python3
"""
This module prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the first 10 hot posts for a given subreddit
    """
    session = requests.Session()
    session.timeout = 5

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    header = {"User-Agent":
              "Reddit First 10 Hot posts v1.0 (https://github.com/Medjai229)"}
    param = {"limit": 10}
    response = session.get(url, headers=header, params=param,
                           allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_posts = data["data"]["children"]
        for post in hot_posts:
            print(post["data"]["title"])
    else:
        print(None)
