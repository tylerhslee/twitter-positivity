"""
Requests the Twitter API to get all tweets made by the user
"""

import tweepy
from auth import API


def extract_text(status):
    if hasattr(status, 'full_text'):
        return status.full_text
    else:
        return status.text


def request_tweets(screen_name, num_tweets=None, include_rts=False, tweet_mode="extended"):
    if num_tweets:
        new_tweets = tweepy.Cursor(
            API.user_timeline,
            id=screen_name,
            include_rts=False,
            tweet_mode=tweet_mode).items(num_tweets)
    else:
        new_tweets = tweepy.Cursor(
            API.user_timeline,
            id=screen_name,
            include_rts=False).items()

    return [extract_text(tweet) for tweet in new_tweets]


def count_tweets(screen_name):
    return API.get_user(screen_name).statuses_count
