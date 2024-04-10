#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
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


def count_words(subreddit, word_list):
    """
    parses the title of all hot articles
    """
    if not word_list:
        return
    hot_list = recurse(subreddit)
    if hot_list:
        a_string = ' '.join(hot_list)
        words_count = list(
                map(
                    lambda w: (w, a_string.count(w)),
                    set(
                        map(
                            lambda x: x.lower(),
                            word_list))))
        words_count = list(
                sorted(
                    words_count,
                    key=lambda item: (-item[1], item[0]),
                    reverse=False))
        words_count = list(
                map(
                    lambda item: '{}: {}'.format(item[0], item[1]),
                    words_count))
        print('\n'.join(words_count))
