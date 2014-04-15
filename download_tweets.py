from twython import Twython

# Import Authenticate Info
from auth import *

# Authenticate
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# import twitter accounts
file = open("accounts.tsv", "rb")

accounts = {}
for line in file:
	parts = line[:-1].split("\t")
	name = parts[0]
	state = parts[1]
	chamber = parts[2]
	party = parts[3]
	account_name = parts[4]
	accounts[account_name] = {
				'state':state ,
				'full_name': name,
				'chamber':chamber,
				'party': party }

file.close()

# get twitter data for user
file = open('tweets.tsv', 'w')

count = 0 # remove this
for user in accounts:
	count += 1 # remove this
	if count % 150 == 0:
		time.sleep(15*60)
    	try:
        	tweets = twitter.get_user_timeline(screen_name=user, count=200)
    	except:
        	continue
   	for tweet in tweets:
        	tweet_txt = tweet['text']
		tweet_time = tweet['created_at']
		utc_offset = str(tweet['user']['utc_offset'])
		mentions = [ m['screen_name'] for m in tweet['entities']['user_mentions']]
        	line = user + "\t" 
		line += accounts[user]['state'] + '\t' 
		line += accounts[user]['party'] + "\t" 
		line += accounts[user]['chamber'] + "\t"
		line += ",".join(mentions) + "\t"
		line += tweet_time + "\t"
		line += utc_offset + "\t"
		line += tweet_txt + '\n'
        	file.write(line.encode("UTF-8"))
	
file.close()

