#!/usr/bin/python3
"""
Function to query Reddit API for subreddit subscriber count.
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subscribers.counter:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0