import tweepy, time, sys
import os
from os import environ


#consumer_key = os.getenv("CONSUMER_KEY")
#consumer_secret = os.getenv("CONSUMER_SECRET")
#access_token = os.getenv("ACCESS_TOKEN")
#access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.description)
print(user.location)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

theleftcanwin = "theleftcanwin.txt"
filename=open(theleftcanwin,'r', errors='replace')
f=filename.readlines()
filename.close()

print('Tweeting every 2 hours...')

for line in f:
    try:
        api.update_status(line)
        print(line)
        time.sleep(7200)#Tweet every 2 hours

    except KeyboardInterrupt:
        sys.exit("KeyboardInterrupt")
    except Exception as e:
        print(e)
        pass
