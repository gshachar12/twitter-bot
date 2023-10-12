
import os
import tweepy

api_key = 'dn7BUM9OBTr705Ve8bEfNspaV'
api_secret = 'zx97MQsUM9JJOsvwrnkvXhcH19zOCJXLUoZXjqoMQPKIYThNsN'
access_token = '1394372084478976008-HeK2aEESu3o7ZVOdfjeuZrwKz996sQ'
access_token_secret = 'Aqi6huIC8PeooUNiz9ExF9bO6WhNU1GRjNRaKYWuLMspC'
bearer_token = r'AAAAAAAAAAAAAAAAAAAAAG%2BNqQEAAAAAZy7C9n%2F1LBWkCARLzQ3z1F%2F' \
               r'q%2BaQ%3DZr1sVWOD9oWpTUD5H3xryI5Wb7ay0qJ1A1KUMZKPLlso70tQwm'
client = tweepy.Client(bearer_token, api_key, api_secret, access_token_secret)
auth=tweepy.OAuthHandler(api_key, api_secret, access_token_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Create a tweet using Tweepy

client.create_tweet(text="#hello")
api.update_status(tweet_text)
