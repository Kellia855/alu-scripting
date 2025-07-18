#!/usr/bin/python3
"""
Recursive function to get all hot article titles of a subreddit.
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:hot.recurse:v1.0 (by /u/yourusername)'
    }
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            hot_list.append(post['data']['title'])

        # Check for next page
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        return None
