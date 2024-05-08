#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/0.1"}

    response = requests.get(url, headers=headers)
    data = response.json()

    return data["data"].get("subscribers", 0)
