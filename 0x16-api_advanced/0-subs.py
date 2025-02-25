#!/usr/bin/python3
"""
Funtion to query the Reddit API and return the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-user-agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
