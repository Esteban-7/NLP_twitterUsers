from twitter_request import get_timeline
from misc_twitter import classify_tweets,tweets_list_to_text,summarize_tweets

def analyse_tweets(user):
    timeline = get_timeline(user)
    timeline_df = timeline["tweets_df"]
    
    timeline_df = classify_tweets(timeline_df)
    
    normal = timeline_df[timeline_df["classification"]==2]
    normal = list(normal["tweet"])
    normal_text = tweets_list_to_text(normal)
    normal_summary = summarize_tweets(normal_text)
    
    offensive = timeline_df[timeline_df["classification"]==1]
    offensive = list(offensive["tweet"])
    offensive_text = tweets_list_to_text(offensive)
    offensive_summary = summarize_tweets(offensive_text)
    
    hate = timeline_df[timeline_df["classification"]==0]
    hate = list(hate["tweet"])
    hate_text = tweets_list_to_text(hate)
    hate_summary = summarize_tweets(hate_text)

    timeline_df['Label'] = timeline_df['classification'].apply(lambda classification: 'Normal' if classification == 2 else 'Offensive' if classification == 1 else 'Hate')

    
    return [timeline_df,normal_summary, offensive_summary, hate_summary]