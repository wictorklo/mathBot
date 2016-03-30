import tweepy
import time
import sys
import re
import math
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

mentions = api.mentions_timeline()
calculatedTweets = []

def calculate(tweet):
	match = re.search(r'([-+]?[0-9]*\.?[0-9]+\s*[\/\+\-\*\^]\s*)+([-+]?[0-9]*\.?[0-9]+)', tweet.text)

	if match and tweet.id not in calculatedTweets:
		print(match.group())
		expression = str(match.group())
		print(expression + " = " + str(eval(expression)))
		api.update_status(expression + " = " + str(eval(expression)) + " @" + str(tweet.user.screen_name), tweet.id)
		calculatedTweets.append(tweet.id)


	elif tweet.id not in calculatedTweets:
		print("Could not find any matches")
		api.update_status("Could not find math expression @" + str(tweet.user.screen_name), tweet.id )
		calculatedTweets.append(tweet.id)


for status in mentions:
	if status.id not in calculatedTweets:
		print(str(status.user.screen_name) + " : " + status.text)
		print(status.id)
		calculate(status)
		print("\n\n")
		#api.update_status("Test reply @" + str(status.user.screen_name), status.id)



#api.update_status("Testing tweet 1", )
time.sleep(3)