import pandas as pd
import os
import pathlib
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go

APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())

df_2 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "mask-use.csv")), dtype={"COUNTYFP": str})
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig_2 = go.Figure()
fig_2 = px.choropleth_mapbox(df_2, geojson=counties, locations='COUNTYFP', color='ALWAYS',
                           color_continuous_scale=["red", "blue"],
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'ALWAYS':'Always'}
                          )
