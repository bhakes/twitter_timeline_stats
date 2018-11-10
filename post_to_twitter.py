# -*- coding: utf-8 -*-

import tweepy as tp
import time
import os
import random

# credentials to login to twitter api
consumer_key = 'X'
consumer_secret = 'X'
access_token = 'X'
access_secret = 'X'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('images')

directory = os.getcwd()

# iterates over pictures in quotes folder
for status in os.listdir('.'):
    f = open(status, 'r')
    api.update_with_media(status)
    f.close()
    y = random.randint(1,101)
    print "I will sleep for " + str(y) +"secs"
    time.sleep(y)
