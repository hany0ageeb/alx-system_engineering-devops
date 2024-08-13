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
        'User-Agent': 'CustomClient/1.0',
    }
    response = requests.get(
        URL,
        headers=headers,
        allow_redirects=False)
    if response.status_code != 200:
        return 0
    response = response.json()
    if 'data' in response:
        return response.get('data').get('subscribers', 0)
    return 0
