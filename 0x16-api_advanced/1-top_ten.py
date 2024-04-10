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
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Custom'}
    params = {'limit': 10, 'show': 'all'}
    response = requests.get(
        URL,
        headers=headers,
        params=params,
        allow_redirects=False)
    if (response.status_code == 200):
        titles = [
            child.get('data').get('title')
            for child in response.json().get('data').get('children')]
        for title in titles:
            print(title)
    else:
        print('None')


if __name__ == '__main__':
    top_ten('Gaza')
