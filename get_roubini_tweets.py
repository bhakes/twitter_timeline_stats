# -*- coding: utf-8 -*-

import tweepy as tp
import time
import os
import random
import urllib2
import json

# credentials to login to twitter api
consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_token = 'XXXX'
access_secret = 'XXXX'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# Only iterate through the first 200 statuses
f= open("timeline.json","a")
cryptoPost = 0
nonCryptoPost = 0
totalTweets = 0
itemCount = 2000
keywords = ['bitcoin', 'Bitcoin', 'crypto', 'ethereum', 'Ethereum', 'Ripple', 'ripple', 'Eth', 'ETH', 'Tether', 'tether', 'blockchain', 'Blockchain', 'dApps', 'S9', 's9', 'BitThumb', 'energy consumption']
for status_list in tp.Cursor(api.user_timeline, id="@hmichellerose").items(itemCount):
    totalTweets += 1
    status = status_list._json
    json_out2 = json.dumps(status['text'], indent=4, sort_keys=True)
    if(any(x in json_out2 for x in keywords) == True):
        cryptoPost += 1
        json_out = json.dumps(status['created_at'], indent=4, sort_keys=True)
        json_out = json_out + " " + json_out2 + "\n"
        f.write(json_out)
f.close()
print "Tweets/RTs mentioning Bitcoin/Crypto/Blockchain: " + str(cryptoPost) + "\nTotal Tweets: " + str(totalTweets)
