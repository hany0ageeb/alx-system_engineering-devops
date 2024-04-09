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
    URL = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit={}'.format(
        subreddit,
        10)
    headers = {'User-Agent': 'Python/1.0(0x16 API)'}
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts:
                print(post['data']['title'])
        except KeyError:
            print('None')
    else:
        print('None')