from twython import Twython

# Import Authenticate Info
from auth import *

# Authenticate
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# import twitter accounts
file = open("accounts.txt", "rb")

accounts = {}
for line in file:
    line_splitted = line.split(',')
    try:
        url = line_splitted[0]
    except:
        pass
    account_name = url.split('/')[-1]
    if account_name == "": continue
    name_title = line_splitted[1].split(' ')
    title = name_title[0]
    name = name_title[1:]
    accounts[account_name] = {'title': title, 'full_name': name}

file.close()

# get twitter data for user
file = open('tweets.txt', 'a')

for user in accounts.keys():
    try:
        tweets = twitter.get_user_timeline(screen_name=user)
    except:
        continue
    for tweet in tweets:
        tweet_txt = tweet['text']
        line = user + '\t' + tweet_txt + '\n'
        file.write(line.encode("UTF-8"))

file.close()