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
    name_title = line_splitted[1].split(' ')
    title = name_title[0]
    name = name_title[1:]

    accounts[account_name] = {'title': title, 'full_name': name}

file.close()

# get twitter data for user

file = open('test.txt', 'a')

for i in range(3):
    user = account_name[i]
    tweets = twitter.get_user_timeline(screen_name=user,count=2)
    #file.write(tweets_json)