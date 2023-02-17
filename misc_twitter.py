from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from transformers import pipeline
from joblib import load
import re
import pandas as pd


def print_score(clf, X_train, y_train, X_test, y_test, train=True):
    if train:
        pred = clf.predict(X_train)
        clf_report = pd.DataFrame(classification_report(y_train, pred, output_dict=True))
        print("Train Result:\n================================================")
        print(f"Accuracy Score: {accuracy_score(y_train, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_train, pred)}\n")
        
    elif train==False:
        pred = clf.predict(X_test)
        clf_report = pd.DataFrame(classification_report(y_test, pred, output_dict=True))
        print("Test Result:\n================================================")        
        print(f"Accuracy Score: {accuracy_score(y_test, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_test, pred)}\n")
        

def clean_tweets(tweet):
    words = re.sub("(?P<url>https?://[^\s]+)"," ",tweet)
    words = re.sub("_","",words)
    words = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z_À-ÿ \t])|(\w+:\/\/\S+)","",words)
    words = re.sub("RT ","",words)
    return words


def tweets_list_to_text(tweets_list):
     #get a list of all tweets, join it in a long string. Divide the string such that the summarizer can read it later. 
    text = '.\n'.join(tweets_list)
    text = re.sub("\n","",text)

    substring_length = 4000

    # Use a list comprehension to create a list of substrings
    substrings = [text[i:i+substring_length] for i in range(0, len(text), substring_length)]
    
    return substrings


def summarize_tweets(substrings):
    #gets a list of substrings, summarizes all the text to create one large summary.

    summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
    total_summary = ""
    for text in substrings:
        summary = summarizer(substrings[0]) #summarize the text
        summary = summary[0]["summary_text"] 
        total_summary = total_summary + summary

    return total_summary
        

def classify_tweets(tweets_df):   
    vectorizer = load("data/vectorizer.joblib")
    
    tweets_transformed =  list(tweets_df["tweet"])
    tweets_transformed =  vectorizer.transform(tweets_transformed).toarray()
    
    model = load("data/xgb_model.joblib")
    predictions = model.predict(tweets_transformed)
    
    tweets_df["classification"] = predictions
    
    return tweets_df


