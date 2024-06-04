#!/usr/bin/python3
"""
This module returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    session = requests.Session()
    session.timeout = 5

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent":
              "Reddit Subscriber Counter v1.0 (https://github.com/Medjai229)"}
    response = session.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    return 0
