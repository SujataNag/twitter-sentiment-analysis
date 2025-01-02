import tweepy
from textblob import TextBlob

api_key= ''
api_secret= ''

access_token=''
access_token_secret=''

auth= tweepy.OAuthHandler(api_key,api_secret)

auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search_tweets('AVENGERS')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print('positive')
    elif analysis.sentiment[0]<0:
        print('Negative')
    else:
        print('Neutral')