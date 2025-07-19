#!/usr/bin/python3

""""
Function that prints the titles of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of 10 hot posts"""
    
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post["data"]["title"])

    except Exception:
        print("None")
