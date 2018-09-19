#! /usr/bin/env python
# coding: utf-8
"""
Get as many sentiment scores from Twitter as possible.
Put them all into a single CSV file.
Profit.
"""
import requests
import time

from auth import API

with open("data/user_ids.txt", "r") as rf:
    data = rf.read().split("\n")[:-1]

with open("data/user_scores.csv", "w") as wf:
    for tweeter_id in data:
        handle = API.get_user(tweeter_id).screen_name
        print("Getting user %s... (%s)" % (handle, tweeter_id))

        try:
            r = requests.get("https://twitter-positivity-dot-tylerlee-portfolio.appspot.com/score?handle=%s" % handle).json()
        except:
            continue    # Internal error - the code is fine, just skip the "special cases"

        if "errors" in r:
            print(r["errors"])  # 401: private users; 425: rate-limit error
            continue

        wf.write("%s,%s,%f\n" % (handle, tweeter_id, r['score']))
        time.sleep(3)   # Avoid rate limit
