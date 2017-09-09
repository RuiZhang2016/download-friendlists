import pandas as pd
import tweepy

class Twitter_API:
	def __init__(self,file):
        	self.accounts = pd.read_csv("accounts.csv")
	        self.N = len(self.accounts.index)

	def get(self,id):
        	auth = tweepy.OAuthHandler(self.accounts['Consumer Key (API Key)'][id], self.accounts['Consumer Secret (API Secret)'][id])
	        auth.set_access_token(self.accounts['Access Token'][id], self.accounts['Access Token Secret'][id])
        	api = tweepy.API(auth)
	        return(api)

	def num(self):
		return(self.N)
	
	def info(self,id):
		print(self.accounts["username/phone"][id])
