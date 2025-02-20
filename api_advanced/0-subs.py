#!/usr/bin/python3
"""DOCUMENTATION"""
import requests


def number_of_subscribers(subreddit):
    """DOCUMENTATION"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    
    return 0
