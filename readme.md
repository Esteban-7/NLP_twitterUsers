 # Authors 
    Sarah Santos 
    Maria Vogli
    Esteban Ortega Lopez

# Analysis of Speech hate per User on twitter. 

    The rise of social media has significantly transformed the way people interact with one another. 
    It has provided a platform for individuals to express themselves and share their views on various subjects. 
    However, social media has also been a breeding ground for hate speech. Hate speech can be defined as any form of communication that is designed to degrade, 
    intimidate, or incite violence against a person or a group of people based on their ethnicity, religion, gender, sexual orientation, or any other characteristic. 
    It is important to keep an eye on hate speech on social media because it can have severe consequences on the targeted individuals or groups. 
    It can cause psychological harm, incite violence, and create an environment of fear and hatred.

    To determine whether a user is being hateful or not, it is necessary to take into account more than one observation. 
    Hate speech is often contextual and subjective, making it difficult to identify. 
    It is essential to examine a user's entire online presence and not just one particular post or comment. 
    Additionally, it is important to consider the intention behind the speech, the severity of the language used, and the impact it may have on the targeted individual or group.
     It is also essential to take into account the cultural and social background of the user and the context in which the speech was made. 
     By considering all these factors, we can develop a more comprehensive understanding of hate speech and take appropriate actions to address it.

     This project aims at identifying the hate speech on twitter based on a powerful Machine Learning algorithm. But rather than focusing on one single tweet made by 
     a user, this apps searches for the last 1000 tweets generated, identifies the hate speech and reports the statistics and brief description of what the user has posted.
    Like this, not only hate speech on singular posts can be studied, but the timeline of usersthemselves. 

    We use a Support Vector Machine Model trained on the database for detection of hatespeech that can be found at https://github.com/SDS-AAU/SDS-master/raw/master/M2/data/twitter_hate.zip
    Later, we use Twitter API to search for the posts that a user has made in the last months. We classify all the tweets by the user according to the predictions of the model. 
    With this, we report the percentage of estimated hate speech in a single user.

    Later, we use a public trained model from Huggin face to summarize the tweets from the different cathegories. We use the model philschmid/bart-large-cnn-samsum (can be found here: https://huggingface.co/philschmid/bart-large-cnn-samsum).
    This model takes input as text and summarizes in a few lines the most important parts of it. 

# NLP class

    Following the topics of the NLP course for the DS2E, we decided to include an analysis on speech hate, but using a different ML algorithm, as well as a different vectorizer 
    to work with the text. We use Twitter API to get access to tweets on real time. In addition we implement a model of summarizing text seen on HugginFace. 

# Requirements

    All the packages needed can be found in the requirements.txt file. 

    Time of processing might be long depending on the spcs of the Machine. Pay attention to the processor and ram while using the app. 
    
# Credentials
    It is necessary to provide Twitter API tokens to the app for it to work. For security and privacy reasons we cannot provide the keys used during development. 
    In this case the credentials.py file is to be saved in the data folder. 

    Two variables are to be set:

    bearer_token = "" #String corresponding to the Twitter API token. 
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    
# Contents
    - The App.py file containst the main Dash App, that is, the main File to be executed. 
    - In the data folder the vocabulary from the vectorizer used as well as the original data can be found, also the joblib files for the developed models. 
    - In the pages folder the scripts for the pages webapp can be found. 
    - The misc_twitter file contains several functions used to handle the text in the different structures for the development of the ML models or the webapp. 
    - The model.ipynb contains the development of the ML classifiers. 
    - On the twitter request there is the code to use the Twitter API to get the ID and the timeline of a given user. 
    - On the twitter results there can be found the function that builds on all the other functions to get the information from twitter, classify using the ML model chosen and provide a simple dataframe for the results to be displayed in the webapp. 