#from data import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import os 
import pathlib

APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

from app_layout import fig_0

app.layout = fig_0


df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "us-states.csv")))

#chloropleth map dataset
df_2 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "mask-use.csv")), dtype={"COUNTYFP": str})
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# us dataset

df_3 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "us.csv")))

# COVID-19 tracker dataset

df_4 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "all-states-history.csv")))

@app.callback(
    [Output('state-cases-bar-graph', 'figure'),Output('mask-use-map','figure'),Output('scatterplot','figure'),Output('bubble-map','figure')],
    [Input('dropdown-1', 'value')])
def update_figure(selected_states):
    new_df_2 = pd.DataFrame()
    new_df = pd.DataFrame()
    for state in selected_states:
        to_append = pd.DataFrame(df[df.state == state])
        new_df = new_df.append(to_append)
        to_append = pd.DataFrame(df_2[df_2.STATE == state])
        new_df_2 = new_df_2.append(to_append)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=new_df['state'], y=new_df['cases'], name='Cases by State', marker_color='rgb(55, 83, 109)'))
    fig.add_trace(go.Bar(x=new_df['state'], y=new_df['deaths'],name='Deaths by State',marker_color='rgb(26, 118, 255)'))
    fig.update_layout(title='Cases and Death Count Per State' ,xaxis_tickfont_size=14, yaxis=dict(title='State',titlefont_size=16,tickfont_size=14,),legend=dict(bgcolor='rgba(255, 255, 255, 0)',bordercolor='rgba(255, 255, 255, 0)'),barmode='group',bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1) # gap between bars of the same location coordinate.


    fig_2 = go.Figure()
    fig_2 = px.choropleth_mapbox(new_df_2, geojson=counties, locations='COUNTYFP', color='ALWAYS',
                           color_continuous_scale=["red", "blue"],
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'ALWAYS':'Always'}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(transition_duration=500)

    fig_3 = px.scatter(new_df, x="deaths", y="cases", size="cases", hover_name="state", size_max=40)
    new_df['text'] = 'state: ' + df['state'] + ' '+'<br>cases: ' + df['cases'].astype(str) + ' ' + '<br>deaths: ' + df['deaths'].astype(str)
    limits = [(0,1000000)]
    colors = ["royalblue","royalblue","royalblue","royalblue","royalblue"]
    scale = 500
    fig_4 = go.Figure()
    for i in range(len(limits)):
        lim = limits[i]
        df_sub = new_df[lim[0]:lim[1]]
        fig_4.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = new_df['longitude'],
        lat = new_df['latitude'],
        text = new_df['text'],
        marker = dict(
            size = new_df['cases']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name =  '{0} - {1}'.format(lim[0],lim[1])))
    fig_4.update_layout(
        title_text = 'COVID-19 cases across the U.S',
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )

    )
    fig_5 = px.line(df_3, x="date", y="cases")  # cases rolling average

    fig_6 = px.line(df_3, x="date", y="deaths")  # deaths rolling average

    fig_7 = px.line(df_4, x="date", y="positive")  # Positive cases by state

    fig_8 = px.line(df_4, x="date", y="hospitalized")  # Hospitalized

    fig_9 = px.line(df_4, x="date", y="hospitalizedCurrently")  # Currently hospitalized

    fig_10 = px.line(df_4, x="date", y="deathIncrease")  # Death increases

    return fig, fig_2, fig_3, fig_4



# positive by state call back
#@app.callback(
    #Output("positive-by-state", "figure"),
    #[Input("dropdown-1", "value")])

#def display_time_series(selected_states):
    #AK = df_4.loc[df_4[selected_states] == selected_states]
    #AK_df = pd.DataFrame(data=AK)

    #fig_7 = px.line(AK_df, x="date", y="positive")
    #return fig_7


if __name__ == '__main__':
    app.run_server(debug=True)
