import tweepy, time, sys
import os
from os import environ


#consumer_key = os.getenv("CONSUMER_KEY")
#consumer_secret = os.getenv("CONSUMER_SECRET")
#access_token = os.getenv("ACCESS_TOKEN")
#access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

sys.stdout.write('19')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

sys.stdout.write('26')

user = api.me()
print(user.name)
print(user.description)
print(user.location)

sys.stdout.write('33')

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

sys.stdout.write('41')

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
