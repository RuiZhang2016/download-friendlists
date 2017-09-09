import pandas as pd
import tweepy
import os
import time
from multiprocessing import Pool
from util import download_friends, extract_users
from twitter_api import Twitter_API

users = extract_users()
apiID = 0
APIs = Twitter_API("accounts.csv")
n = len(users)

for i in range(int(1*n/5),int(2*n/5)):
    downloadSuccess = download_friends(users[i],APIs.get(apiID),'../friend-lists/')
    if downloadSuccess==0:
        apiID = (apiID+1)%APIs.num()
