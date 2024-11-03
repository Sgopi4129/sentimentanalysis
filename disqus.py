import requests
from textblob import TextBlob

# Step 1: Configure Disqus API credentials
DISQUS_API_KEY = "your_disqus_api_key"
FORUM_NAME = "example_forum"  # Replace with the Disqus forum name


def fetch_disqus_comments(forum_name, thread_id=None, limit=20):
    """
    Fetches comments from a Disqus forum or thread and performs sentiment analysis.

    Args:
        forum_name (str): The Disqus forum shortname to retrieve comments from.
        thread_id (str, optional): ID of the specific thread. If None, fetches the latest comments.
        limit (int): Number of comments to fetch.

    Returns:
        list of tuples: Each tuple contains the comment text and sentiment polarity.
    """
    comments_data = []
    url = "https://disqus.com/api/3.0/posts/list.json"
    params = {
        "api_key": DISQUS_API_KEY,
        "forum": forum_name,
        "limit": limit,
        "thread": thread_id,
        "order": "desc"
    }

    # Step 2: Send GET request to fetch comments
    response = requests.get(url, params=params)
    if response.status_code == 200:
        comments = response.json().get("response", [])
        for comment in comments:
            comment_text = comment["message"]

            # Step 3: Perform sentiment analysis
            sentiment = TextBlob(comment_text).sentiment.polarity
            comments_data.append((comment_text, sentiment))

            print(f"Comment: {comment_text[:100]}...")  # Display first 100 characters
            print(f"Sentiment Polarity: {sentiment}\n")
    else:
        print("Failed to fetch comments:", response.json())

    return comments_data


# Example usage
comments_data = fetch_disqus_comments(FORUM_NAME, limit=10)

# Analyzing sentiment distribution
positive = sum(1 for _, sentiment in comments_data if sentiment > 0)
neutral = sum(1 for _, sentiment in comments_data if sentiment == 0)
negative = sum(1 for _, sentiment in comments_data if sentiment < 0)

print(f"Positive comments: {positive}")
print(f"Neutral comments: {neutral}")
print(f"Negative comments: {negative}")
