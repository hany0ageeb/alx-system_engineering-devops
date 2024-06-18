#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users,
total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    query the reddit API and returns the number of
    subscribers for a given subreddit
    Args:
        subreddit(str): the name of subreddit to query about
    Return:
        int: the number of subscribers or 0
    """
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Safari/573.36',
        'Accept': 'application/json',
    }
    response = requests.get(
        URL,
        headers=headers,
        allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json().get('data', {'subscribers': 0})
            return data.get('subscribers', 0)
        except requests.exceptions.JSONDecodeError:
            return 0
    return 0

