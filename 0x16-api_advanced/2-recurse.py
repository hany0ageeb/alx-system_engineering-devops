#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Retrieves a list of hot posts from a given subreddit."""
    headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    if after is None:
        URL = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(
                subreddit)
    else:
        URL = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
                subreddit,
                after)
    response = requests.get(
        URL,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code != 200:
        return hot_list if hot_list else None
    data = response.json()['data']
    hot_list.extend(list(map(lambda x: x['data']['title'], data['children'])))
    after = data['after']
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
