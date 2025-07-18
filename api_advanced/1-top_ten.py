#!/usr/bin/python3

"""
function that prints the titles of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'CustomUserAgent/0.1'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

    except Exception:
        print(None)
