import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc


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
            dcc.Input(id = "input_search",type="search"),
            html.Button('Submit', id='submit-val')
        ], width= 5),
    ]),

    dbc.Row([
        dcc.Graph(id='pie_chart', figure={}),
    ]),

    dbc.Row([
        dbc.Col([
            html.Label("The quick recap of normal tweets:"),
            dcc.Markdown(id="normal_recap",children=[])
        ], width= 4),

        dbc.Col([
            html.Label("The quick recap of offensive tweets:"),
            dcc.Markdown(id="offensive_recap",children=[])
        ], width= 4),

        dbc.Col([
            html.Label("The quick recap of hate tweets:"),
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
    [#Output(component_id='pie_chart', component_property='figure'),
    Output(component_id='normal_recap', component_property='children'),
    Output(component_id='offensive_recap', component_property='children'),
    Output(component_id='hate_recap', component_property='children')],
    [Input(component_id='input_search', component_property='value')]
)
def update_graph(user):

    #pie_works = px.pie(dff, values = "works_count", names = "type",title = "Academic production per type of institution",
    #                    labels= {"works_count":"Publications","cited_by_count":"Citations"})


                        
    return ["normal","offensive","hate"]
