from twython import Twython, TwythonError
import json



APP_KEY = 'bzg3g0DgsVr4C39AbE9lKhZWY'
APP_SECRET = 'K21FVfQxdlEHgnpNvw2d33bgyoDghdygViwsje0OVgviQ0tn57'
OAUTH_TOKEN = "1456459339-TR1txZkGZ6MDWaHuTKHAZTO5ZifoQrCt3DV9XaM"
OAUTH_TOKEN_SECRET = "YePHmObB5dnY5pMG4HhkJnTjLKoYIgI7frDI4WMSCLTwT"


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


users = []
lines = file("accounts.txt").read().split("\n")[:-1]
for line in lines:
	(twname, name) = line.split("\t")
	users.append(twname)	



found_count = 0

for user in users:
	print user
	#try:
	user_timeline = twitter.get_user_timeline(screen_name=user)
	#except TwythonError:
	#	print "not found"
	#	continue
	print "found"
	found_count += 1


print "found %s of %s" % (found_count,len(users))


