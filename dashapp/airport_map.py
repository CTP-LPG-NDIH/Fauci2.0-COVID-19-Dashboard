import pandas as pd
import os
import pathlib
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go

APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())

df_6 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "large_ap.csv")))

df_6['text'] = df_6['name'] + ' ' + df_6['Volume'].astype(str)
limits = [(0,1000000)]
colors = ["royalblue","royalblue","royalblue","royalblue","royalblue"]
scale = 10000

fig_11 = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df_6[lim[0]:lim[1]]
    fig_11.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['longitude_deg'],
        lat = df_sub['latitude_deg'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['Volume']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig_11.update_layout(
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

