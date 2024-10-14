import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid = []

    for tweet_id, content in zip(tweets["tweet_id"], tweets["content"]):
        if len(str(content)) > 15:
            invalid.append(int(tweet_id))

    return pd.DataFrame({"tweet_id": invalid})
