#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a
given subreddit.
If the subreddit is invalid or there is an error, prints None.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)
