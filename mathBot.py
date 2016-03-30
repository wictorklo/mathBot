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

def calculate(text):
	match = re.search(r'([-+]?[0-9]*\.?[0-9]+\s*[\/\+\-\*\^]\s*)+([-+]?[0-9]*\.?[0-9]+)', tweet)

	if match:
		print(match.group())
		expression = str(match.group())
		print(expression + " = " + str(eval(expression)))


	else:
		print("Could not find any matches")


for status in mentions:
	print(str(status.user.screen_name) + " : " + status.text)
	print(status.id)
	tweet = status.text
	calculate(tweet)
	print("\n\n")
	calculatedTweets.append(status.id)



#api.update_status("Testing tweet 1")
time.sleep(3)