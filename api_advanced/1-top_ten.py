import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    If the subreddit is invalid or doesn't exist, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.top_ten:v1.0 (by /u/yourusername)"}

    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if posts:
            for i, post in enumerate(posts[:10]):
                print(post["data"]["title"])
        else:
            print(None)
    else:
        print(None)

# Example usage
top_ten("python")

