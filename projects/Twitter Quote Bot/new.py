import tweepy
import requests
import time
import random

def queryRepeatedly():
    while True:
        try:
           client = tweepy.Client(consumer_key='###',consumer_secret='###',access_token='###',access_token_secret='##')
           for i in range(1,99999):
                response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
                json_data = response.json()
                data = json_data['data']
                #print(data[0]['quoteText'])
                hey = data[0]['quoteText']
                tweet = client.create_tweet(text=hey,quote_tweet_id=random.randint(1,999))
                print(tweet)
                time.sleep(30)
        except Exception as e:
            print(e)
            continue
            time.sleep(30)
        time.sleep(30)
a=0
while a <=10:
  queryRepeatedly()