import tweepy
import config
from datetime import datetime, timedelta

auth = tweepy.OAuthHandler(config.consumer_token, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


def get_tweets(q, lang):
    return api.search(q=q, lang=lang, tweet_mode="extended", count=100)


time_diff = timedelta(hours=24)
curr_date_time = datetime.now()

query = '@hermesparcels missing'
language = 'en'

results = get_tweets(query, language)

for result in results:
    if not hasattr(result, "retweeted_status"):
        if result.created_at >= curr_date_time - time_diff:
            print(result.created_at)
            print(result.user.screen_name)
            print(result.full_text)
            print(result.favorite_count)