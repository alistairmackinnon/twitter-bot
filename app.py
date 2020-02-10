import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_token, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)