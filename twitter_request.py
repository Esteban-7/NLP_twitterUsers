import data.credentials as credentials
from misc_twitter import clean_tweets
import requests
import time 
import pandas as pd


headers = credentials.headers


def get_id(user):
    search_id_url = f'https://api.twitter.com/2/users/by/username/{user}'
    response_user_id = requests.request("GET",search_id_url, headers=headers)
    user_id = response_user_id.json()
    user_id = user_id['data']['id']
    return user_id


def get_timeline(user):

    user_id = get_id(user)
    
    timeline_url=f"https://api.twitter.com/2/users/{user_id}/tweets"
    tweets = []

    start = 0
    for iteration in range(0,2):
        time.sleep(2)

        if start ==0:
            query_params = {"exclude":"retweets,replies",
                            "max_results": 100}
        else:
            query_params = {"exclude":"retweets,replies",
                            "max_results": 100,
                            "pagination_token":next_token}

    response = requests.request("GET", timeline_url, headers=headers, params = query_params)

    if response.status_code == 429:
        time.sleep(60)
        response = requests.request("GET", timeline_url, headers=headers, params = query_params)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


    r = response.json()
    next_token = r["meta"]["next_token"]

    for tweet in r["data"]:
        clean_tweet = clean_tweets(tweet["text"])
        tweets.append(clean_tweet)
    
    tweets_df = pd.DataFrame(tweets)
    tweets_df.columns = ["tweet"]
    
    return {"tweets":tweets, "tweets_df":tweets_df}