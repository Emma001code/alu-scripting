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
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # If the subreddit is invalid or a redirect occurs, the status
        # won't be 200.
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)
