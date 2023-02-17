import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page, commonly used as name of link
                   title='home',  # title that appears on browser's tab
                   description='home')


layout = html.Div([
    html.H1("Home", style={'text-align': 'left'}),

    html.H4("Purpose", style={'text-align': 'left'}),
    dcc.Markdown("""
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
    
    """),

    html.H4("The model", style={'text-align': 'left'}),
    dcc.Markdown("""
    We use a Support Vector Machine Model trained on the database for detection of hatespeech that can be found at https://github.com/SDS-AAU/SDS-master/raw/master/M2/data/twitter_hate.zip
    Later, we use Twitter API to search for the posts that a user has made in the last months. We classify all the tweets by the user according to the predictions of the model. 
    With this, we report the percentage of estimated hate speech in a single user.

    
    """),

    html.H4("The code", style={'text-align': 'left'}),
    dcc.Markdown("""
    Code for the ML model and the webapp can be found at:
    
    """),
    
])
