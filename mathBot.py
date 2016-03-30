import tweepy
import time
import os
import sys
import re
import math
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

def calculate(tweet):
        match = re.search(r'([-+]?[0-9]*\.?[0-9]+\s*[\/\+\-\*\^]\s*)+([-+]?[0-9]*\.?[0-9]+)', tweet.text)
        if '^' in match.group():
                match.group().replace('^', '**')
        if match and str(tweet.id) not in calculatedTweets:
                calculatedTweets.append(str(tweet.id))
                print(match.group())
                expression = str(match.group())
                try:
                        print(expression + " = " + str(eval(expression)))
                except ZeroDivisionError:
                        api.update_status("I would prefer if you could, like, not divide by 0? @" + str(tweet.user.screen_name), tweet.id)
                        return
                
                try:
                        api.update_status(expression + " = " + str(eval(expression)) + " @" + str(tweet.user.screen_name), tweet.id)

                except tweepy.error.TweepError as e:
                        api.update_status("Error: " + str(e) + " @" + str(tweet.user.screen_name), tweet.id)
                        return

        elif str(tweet.id) not in calculatedTweets:
                calculatedTweets.append(str(tweet.id))
                print("Could not find any matches")
                api.update_status("Could not find math expression @" + str(tweet.user.screen_name), tweet.id )
        time.sleep(60)

while 1==1:
        try:
                mentions = api.mentions_timeline(count = 5)

        except tweepy.error.RateLimitError:
                time.sleep(300)

        try:
                mentions = api.mentions_timeline(count = 5)

        except tweepy.error.RateLimitError:
                time.sleep(300)

        if not os.path.exists('repliedTweets.txt'):
                open('repliedTweets.txt', 'w').close()

        with open('repliedTweets.txt', 'rU') as in_file:
                calculatedTweets = str(in_file.read()).split('\n')


        for status in mentions:
                if str(status.id) not in calculatedTweets:
                        print(str(status.user.screen_name) + " : " + status.text)
                        print(status.id)
                        calculate(status)
                        print("\n\n")

        with open('repliedTweets.txt', 'w', ) as out_file:
                out_file.write('\n'.join(calculatedTweets))

        #api.update_status("Testing tweet 1", )
        print("Finished a run")
        time.sleep(60)
