#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of hot articles,
and prints a sorted count of given keywords.
"""
import requests
import re


def count_words(subreddit, word_list, after=None, word_count=None):
"""
Recursively counts keywords in hot article titles from a subreddit.
"""
    if word_count is None:
        # Initialize word counts with lowercase keys
        word_count = {}
        for word in word_list:
            lw = word.lower()
            word_count[lw] = word_count.get(lw, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:keyword.counter:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post['data']['title'].lower()
            words = re.findall(r'\b\w+\b', title)  # Only whole words, no punctuation

            for w in words:
                if w in word_count:
                    word_count[w] += 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # All data processed, now sort and print
            filtered = {k: v for k, v in word_count.items() if v > 0}
            sorted_counts = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    except Exception:
        return
