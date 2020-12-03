import pandas as pd
import os
import pathlib
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go

APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())

df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "us-states.csv")))

df['text'] = 'state: ' + df['state'] + ' '+'<br>cases: ' + df['cases'].astype(str) + ' ' + '<br>deaths: ' + df['deaths'].astype(str)
limits = [(0,1000000)]
colors = ["royalblue","royalblue","royalblue","royalblue","royalblue"]
scale = 500

fig_4 = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig_4.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df['longitude'],
        lat = df['latitude'],
        text = df['text'],
        marker = dict(
            size = df['cases']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig_4.update_layout(
        title_text = 'COVID-19 cases across the U.S',
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )