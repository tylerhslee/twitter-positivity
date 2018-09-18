"""
Authentication for Twitter API
"""
import os
import yaml
import tweepy

cpath = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(cpath, 'conf.yaml'), 'r') as rf:
    tcfg = yaml.load(rf)['twitter-config']

consumer_key = tcfg['consumer-key']
consumer_secret = tcfg['consumer-secret']
access_token = tcfg['access-token']
access_token_secret = tcfg['access-token-secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)
