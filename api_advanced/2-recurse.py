#!/usr/bin/python3

"""
Recursive function to get all hot article titles of a subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are found
    for the given subreddit, the function returns None.
    """
    if hot_list is None:
        hot_list = []

    headers = {'User-agent': 'python:recurse:v1.0 (by /u/fakeuser)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        hot_list.append(child.get('data', {}).get('title'))

    after = data.get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)

