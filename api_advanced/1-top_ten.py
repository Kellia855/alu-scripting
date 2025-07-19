#!/usr/bin/python3

"""
Module that defines a recursive function to retrieve all hot article titles
from a given subreddit using Reddit's API.
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post["data"]["title"])

    except Exception:
        return None
