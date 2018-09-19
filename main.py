#! /usr/bin/env python3
# coding: utf-8
 
"""
Test script
"""
import hug

from twitter import request_tweets, count_tweets, follow_followers
from tweepy.error import TweepError
from nlp.processor import lemmatize, compute_score


@hug.get()
def score(handle: str) -> dict:
    """
    Responds with the sentiment score of the user.

    Args:
        handle (str): Twitter handle of the user

    Returns: The sentiment score of the user. 404 if the user is not found.
    """
    if handle[0] != "@":
        handle = "@" + handle;
    try:
        tweets = request_tweets(handle, num_tweets=10)
        lemmatized = lemmatize(" ".join(request_tweets(handle, num_tweets=10)))
        return {
            "score": compute_score(lemmatized),
            "handle": handle
        }
    except TweepError as e:
        return {
            "errors": str(e)
        }


@hug.get('/tweets')
def fetch_tweets(handle: str, num_tweets: int) -> dict:
    """
    Args:
        handle     (str): Twitter handle of the user
        num_tweets (int): Number of tweets to fetch

    Returns: A list of all tweets. An empty list if the user does not exist.
    """
    if handle[0] != "@":
        handle = "@" + handle;
    try:
        return {
            "tweets": request_tweets(handle, num_tweets=num_tweets),
            "handle": handle
        }
    except TweepError:
        return {
            "errors": { "handle": "The user {} does not exist".format(handle) }
        }


@hug.get('/count')
def count_num_tweets(handle: str) -> dict:
    """
    Counts the number of tweets the user has posted.

    Args:
        handle (str): Twitter handle of the user

    Returns: number of tweets. -1 if the user does not exist.
    """
    if handle[0] != "@":
        handle = "@" + handle;
    try:
        return {
            "count": count_tweets(handle),
            "handle": handle
        }
    except TweepError:
        return {
            "errors": { "handle": "The user {} does not exist.".format(handle) }
        }


@hug.get('/list')
def find_many_tweeters() -> dict:
    """
    Returns:
        A list of many, many tweeters
    """
    ret = []
    cursor = follow_followers("bluebeagle2")
    for ids in cursor:
        ret.extend(ids)
    return ret


app = __hug_wsgi__

if __name__ == '__main__':
    print(find_many_tweeters())
