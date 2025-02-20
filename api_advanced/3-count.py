#!/usr/bin/python3
"""
This script defines a function `count_words` that counts the occurrences
of specific words in the titles of hot posts from a given subreddit.
"""

import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """
    Recursively counts the occurrences of each word in word_list in
    the titles of hot posts from a given subreddit.
    """

    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after, "limit": 100}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json()["data"]
    children = data["children"]
    after = data["after"]

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(
                word_lower, 0
            ) + title.split().count(word_lower)

    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(
            word_count.items(),
            key=lambda kv: (-kv[1], kv[0])
         )
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")
