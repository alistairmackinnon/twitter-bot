import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_token, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

# shs
query = '#scotrail'
language = 'en'

results = api.search(q=query, lang=language, tweet_mode="extended", count=100)

for result in results:
    if not hasattr(result, "retweeted_status"):
        print(result.user.screen_name)
        print(result.full_text)
        print(result.favorite_count)

