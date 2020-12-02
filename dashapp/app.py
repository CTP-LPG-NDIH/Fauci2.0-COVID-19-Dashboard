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



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

from death_case_graph import fig_0

app.layout = fig_0

#callbacks
df = pd.read_csv('/Users/nick/github/Fauci2.0-COVID-19-Dashboard/data/us-states.csv')
#chloropleth map dataset
df_2 = pd.read_csv('/Users/nick/github/Fauci2.0-COVID-19-Dashboard/data/mask-use.csv', dtype={"COUNTYFP": str})
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

@app.callback(
    Output('state-cases-bar-graph', 'figure'),Output('mask-use-map','figure'),Output('scatterplot','figure'),Output('bubble-map','figure'),
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
    fig_2 = px.choropleth_mapbox(new_df_2, geojson=counties, locations='COUNTYFP', color='NEVER',
                               color_continuous_scale=["blue", "red"],
                               range_color=(0, 0.5),
                               mapbox_style="carto-positron",
                               zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               labels={'NEVER':'Never'}
                              )
    fig_2.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title='No mask use by county')
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
    return fig, fig_2,fig_3,fig_4



if __name__ == '__main__':
    app.run_server(debug=True)
