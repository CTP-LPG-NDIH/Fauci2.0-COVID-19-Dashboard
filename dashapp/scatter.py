import pandas as pd
import os
import pathlib
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go



APP_PATH = str(pathlib.Path(__file__).parent.resolve().parent.resolve())

df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "us-states.csv")))
fig_3 = px.scatter(df, x="deaths", y="cases", size="cases", hover_name="state", size_max=40)




