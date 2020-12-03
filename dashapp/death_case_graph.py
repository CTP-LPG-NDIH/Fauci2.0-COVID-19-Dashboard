
# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

#Plotly Libraries
import plotly.express as px
import plotly.graph_objects as go

# Other Libraries
from urllib.request import urlopen
import json

import os
import pathlib
# us-states dataset
APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())

df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "us-states.csv")))


fig = go.Figure()
fig.add_trace(go.Bar(x=df['state'],
                y=df['cases'],
                name='Cases by State',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=df['state'],
                y=df['deaths'],
                name='Deaths by State',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='Cases and Death Count Per State'
    ,xaxis_tickfont_size=14,
    yaxis=dict(
        title='State',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(

        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})





# COVID-19 tracker dataset

df_4 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "all-states-history.csv")))












fig_7 = px.line(df_4, x="date", y="positive") # Positive cases by state

fig_8 = px.line(df_4, x="date", y="hospitalized") # Hospitalized

fig_9 = px.line(df_4, x="date", y="hospitalizedCurrently")  # Currently hospitalized

fig_10 = px.line(df_4, x="date", y="deathIncrease") # Death increases


