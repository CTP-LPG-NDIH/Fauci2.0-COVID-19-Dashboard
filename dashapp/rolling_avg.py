import pandas as pd
import os
import pathlib
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go


APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())

df_3 = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "us.csv")))

fig_5 = px.line(df_3, x="date", y="cases") # cases rolling average

fig_6 = px.line(df_3, x="date", y="deaths") # deaths rolling average