#!/usr/bin/python3
"""
Module to recursively fetch all hot post titles of a subreddit using Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of all hot article
    titles for a given subreddit.

    If the subreddit is invalid or there are no posts, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    if not posts:
        return hot_list if hot_list else None

    hot_list.extend(post["data"]["title"] for post in posts)

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
