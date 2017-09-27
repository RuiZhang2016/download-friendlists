import os
import tweepy
import time

def download_friends(user, API, mydir):
	print('Downloading '+user)
	filename = mydir + user + '.txt'
	if not os.path.isfile(filename):
		friendIDs = []
		try:
			for page in tweepy.Cursor(API.friends_ids, user_id = user,monitor_rate_limit=True, wait_on_rate_limit=True).pages():
				friendIDs.extend(page)
			f = open(filename, 'w')
			for item in friendIDs:
				f.write("%s\n" % item)
			f.close()
			print('Done')
			return(0)
		except tweepy.TweepError as e:
			print(e)
			if e.api_code == 326:
				return(0)
			time.sleep(10)
			return(-1)
	else:
		print('Existing')
		return 1

def extract_users():
	mydir = "../cascades/general/"
	files = os.listdir(mydir)
	nfiles = len(files)
	userIds = []

	for fileId in range(nfiles):
		file = files[fileId]
		with open(mydir+file) as f:
			content = f.readlines()
			if len(content) < 5: continue

			content = [ line.replace("\"","") for line in content]
			content = [ line.split(" ") for line in content]
			userIds.extend([ line[0] for line in content[1:]])
	return list(set(userIds))
