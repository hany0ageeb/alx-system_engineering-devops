#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of first 10 hot posts
    Args:
        reddit(string): the subreddit to query about
    Return:
        None
    """
    URL = 'https://www.reddit.com/r/{}/.json?sort=top&limit=10'.format(
        subreddit)
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
    response = requests.get(
        URL,
        headers=headers,
        allow_redirects=False)
    if (response.status_code == 200):
        titles = [
            child.get('data').get('title')
            for child in response.json().get('data').get('children')]
        for title in titles:
            print(title)
    else:
        print('None')
