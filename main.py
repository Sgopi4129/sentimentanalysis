import praw
from textblob import TextBlob

reddit = praw.Reddit(
    client_id="lY5xHvYoMTp2Xy3-9vhaUA",
    client_secret="6jYLLLzro57qVu_hveKKyw-rBN0pKg",
    user_agent="u/Relative-List-604"
)


def fetch_reddit_comments(subreddit_name, post_limit=10, comment_limit=20):
    comments_data = []

    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.top(limit=post_limit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments[:comment_limit]:
            # Extract comment text
            comment_text = comment.body

            # Step 3: Perform sentiment analysis
            sentiment = TextBlob(comment_text).sentiment.polarity
            comments_data.append((comment_text, sentiment))

            print(f"Comment: {comment_text[:100]}...")
            print(f"Sentiment Polarity: {sentiment}\n")

    return comments_data



comments_data = fetch_reddit_comments("antiwork", post_limit=10, comment_limit=20)

# Analyzing sentiment distribution
positive = sum(1 for _, sentiment in comments_data if sentiment > 0)
neutral = sum(1 for _, sentiment in comments_data if sentiment == 0)
negative = sum(1 for _, sentiment in comments_data if sentiment < 0)

print(f"Positive comments: {positive}")
print(f"Neutral comments: {neutral}")
print(f"Negative comments: {negative}")
