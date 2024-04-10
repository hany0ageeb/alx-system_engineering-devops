#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Custom'
    }
    params = {
        'after': after,
        'limit': 100,
    }
    response = requests.get(
        URL,
        headers=headers,
        params=params,
        allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get('data')
    after = results.get('after')
    for itm in results.get('children'):
        hot_list.append(itm.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list