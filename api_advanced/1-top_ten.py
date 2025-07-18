#!/usr/bin/python3
"""
Function that prints the titles of the first 10 hot posts of a subreddit.
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:topten.fetcher:v1.0 (by /u/yourusername)'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)
