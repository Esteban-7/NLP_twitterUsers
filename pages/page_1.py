import dash
from dash import dcc, html, callback, Output, Input, State 
import plotly.express as px
import dash_bootstrap_components as dbc
from twitter_results import analyse_tweets


# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/search',  # '/' is home page and it represents the url
                   name='Search user',  # name of page, commonly used as name of link
                   title='search',  # title that appears on browser's tab
                   description='search')


layout = dbc.Container([
    
    html.Br(),
    
    dbc.Row([
        html.H4("Search Twitter user", style={'text-align': 'Left'})
    ]),
    
    html.Br(),

    dbc.Row([

        dbc.Col([
            html.Label('User:'),
            html.Br(),
            dcc.Input(id = "input_search",type="search",value="elonmusk"),
            html.Button('Submit', id='submit-val')
        ], width= 5),
    ]),

    dbc.Row([
        dcc.Graph(id='pie_chart', figure={}),
        dcc.Markdown(id="number_tweets",children=[]),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown("**A quick recap of normal tweets:**"),
            dcc.Markdown(id="normal_recap",children=[])
        ], width= 4),

        dbc.Col([
            dcc.Markdown("**A quick recap of offensive tweets:**"),
            dcc.Markdown(id="offensive_recap",children=[])
        ], width= 4),

        dbc.Col([
            dcc.Markdown("**A quick recap of hate tweets:**"),
            dcc.Markdown(id="hate_recap",children=[])
        ], width= 4),

        
    ]),

    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row([
        dcc.Markdown("""
            **Instructions:**
            Copy and paste the username from twitter into the search box. Click on the botton to run the analysis. 
            """) 
    ]),
    
    html.Br(),
])


@callback(
    [Output(component_id='pie_chart', component_property='figure'),
    Output(component_id='normal_recap', component_property='children'),
    Output(component_id='offensive_recap', component_property='children'),
    Output(component_id='hate_recap', component_property='children'),
    Output(component_id="number_tweets", component_property="children")],
    [Input(component_id='submit-val', component_property='n_clicks')],
    [State(component_id = "input_search", component_property = "value")]
)
def update_graph(n_clicks,user):
    print(n_clicks)
    
    results = analyse_tweets(user)
    print(results[0])
    counts = results[0]['Label'].value_counts().reset_index()
    counts.columns = ['value', 'count']
    pie_tweets = px.pie(counts, values = "count", names = "value",title = f"Distribution of the types of Tweets of the user: {user}")

    normal_text = results[1]
    offensive_text = results[2]
    hate_text = results[3]

    print(normal_text)

    number_of_tweets = str(len(results[0]))
    number_of_tweets = f"Total tweets analized: {number_of_tweets}"
                        
    return [pie_tweets,normal_text,offensive_text,hate_text,number_of_tweets]




