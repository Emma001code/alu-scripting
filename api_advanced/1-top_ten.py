#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for a given subreddit.
    Prints None if the subreddit is invalid or has no posts.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    headers = {'User-Agent': 'My User Agent 1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)  # No posts found
        else:
            print(None)  # Invalid subreddit or other error
    except Exception:
        print(None)  # Catch unexpected errors

