"""
Test script
"""
import hug

from twitter import request_tweets, count_tweets
from nlp.processor import lemmatize, compute_score


@hug.post('/')
def score(handle: str):
    tweets = lemmatize(" ".join(request_tweets(handle, num_tweets=10)))
    return compute_score(tweets)


@hug.post('/tweet')
def fetch_tweets(handle: str, num_tweets: int):
    return request_tweets(handle, num_tweets=num_tweets)


@hug.post('/count')
def count_num_tweets(handle: str):
    return count_tweets(handle)


if __name__ == '__main__':
    print(score('realDonaldTrump'))
