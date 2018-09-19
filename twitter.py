"""
Requests the Twitter API to get all tweets made by the user
"""

import tweepy
import time

from auth import API


def extract_text(status: str) -> str:
    """
    Get the actual content of each tweet.

    Args:
        status (str): Tweepy Status object

    Returns: the content of the tweet
    """
    if hasattr(status, 'full_text'):
        return status.full_text
    else:
        return status.text


def request_tweets(screen_name: str, num_tweets=0, include_rts=False, tweet_mode="extended") -> list:
    """
    Talk to the Twitter API to get a list of tweets.

    Args:
        screen_name  (str): The screen name of the user
        num_tweets   (int): Number of tweets to request.
        include_rts (bool): Whether to fetch retweets as well
        tweet_mode   (str): Defaults to "extended" for long tweets

    Returns:
        A list of all tweets
    """
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


def count_tweets(screen_name: str) -> int:
    return API.get_user(screen_name).statuses_count


def follow_followers(seed: str) -> list:
    """
    Collects a lot of Twitter handles by tracking down followers of followers.

    Args:
        seed (str): Screen name of the first tweeter that sets off the chain

    Returns: List of Twitter handles
    """
    ids = []
    return tweepy.Cursor(
            API.followers_ids,
            screen_name=seed).pages()
