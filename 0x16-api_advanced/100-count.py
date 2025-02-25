#!/usr/bin/python3
"""
Module that recursively queries the Reddit API, parses post titles,
and counts occurrences of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses titles of all hot articles,
    and prints a sorted count of given keywords.

    - subreddit: The subreddit to query.
    - word_list: A list of words to count in titles.
    - after: The pagination parameter for recursion.
    - word_count: Dictionary tracking occurrences of each keyword.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    if not posts:
        return print_results(word_count)

    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    for post in posts:
        title = post["data"]["title"].lower().split()
        for word in word_count:
            word_count[word] += title.count(word)

    if after:
        return count_words(subreddit, word_list, after, word_count)

    print_results(word_count)


def print_results(word_count):
    """
    Prints the word occurrences in descending order by count,
    then alphabetically in ascending order if counts match.
    """
    sorted_words = sorted(
        word_count.items(), key=lambda item: (-item[1], item[0])
    )
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")
