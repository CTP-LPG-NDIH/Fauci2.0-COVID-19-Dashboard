
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


# us-states dataset
df = pd.read_csv('/Users/Isaiah/Desktop/Fauci2.0-COVID-19-Dashboard/data/us-states.csv')

# mask-use dataset
df_2 = pd.read_csv('/Users/Isaiah/Desktop/Fauci2.0-COVID-19-Dashboard/data/mask-use.csv', dtype={"COUNTYFP": str})
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# us dataset
df_3 = pd.read_csv('/Users/Isaiah/Desktop/Fauci2.0-COVID-19-Dashboard/data/us.csv')

# COVID-19 tracker dataset
df_4 = pd.read_csv('/Users/Isaiah/Desktop/Fauci2.0-COVID-19-Dashboard/data/all-states-history.csv')


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

fig_2 = go.Figure()
fig_2 = px.choropleth_mapbox(df_2, geojson=counties, locations='COUNTYFP', color='ALWAYS',
                           color_continuous_scale=["red", "blue"],
                           range_color=(0, 1),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'ALWAYS':'Always'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


fig_3 = px.scatter(df, x="deaths", y="cases", size="cases", hover_name="state", size_max=40)



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


fig_5 = px.line(df_3, x="date", y="cases") # cases rolling average

fig_6 = px.line(df_3, x="date", y="deaths") # deaths rolling average

fig_7 = px.line(df_4, x="date", y="positive") # Positive cases by state

fig_8 = px.line(df_4, x="date", y="hospitalized") # Hospitalized

fig_9 = px.line(df_4, x="date", y="hospitalizedCurrently")  # Currently hospitalized

fig_10 = px.line(df_4, x="date", y="deathIncrease") # Death increases


# App Layout

fig_0 = html.Div(children=[
    html.H1(children='Covid19 dashboard'),

    html.Div(children=''' '''),
    html.Label(''),
    dcc.Dropdown(
    	id='dropdown-1',
        options=[
       		{'label': 'Alabama','value': 'Alabama'},
			{'label': 'Alaska','value': 'Alaska'},
			{'label': 'Arizona','value': 'Arizona'},
			{'label': 'Arkansas','value': 'Arkansas'},
			{'label': 'California','value': 'California'},
			{'label': 'Colorado','value': 'Colorado'},
			{'label': 'Connecticut','value': 'Connecticut'},
			{'label': 'Delaware','value': 'Delaware'},
			{'label': 'District of Columbia','value': 'District of Columbia'},
			{'label': 'Florida','value': 'Florida'},
			{'label': 'Georgia','value': 'Georgia'},
			{'label': 'Guam','value': 'Guam'},
			{'label': 'Hawaii','value': 'Hawaii'},
			{'label': 'Idaho','value': 'Idaho'},
			{'label': 'Illinois','value': 'Illinois'},
			{'label': 'Indiana','value': 'Indiana'},
			{'label': 'Iowa','value': 'Iowa'},
			{'label': 'Kansas','value': 'Kansas'},
			{'label': 'Kentucky','value': 'Kentucky'},
			{'label': 'Louisiana','value': 'Louisiana'},
			{'label': 'Maine','value': 'Maine'},
			{'label': 'Maryland','value': 'Maryland'},
			{'label': 'Massachusetts','value': 'Massachusetts'},
			{'label': 'Michigan','value': 'Michigan'},
			{'label': 'Minnesota','value': 'Minnesota'},
			{'label': 'Mississippi','value': 'Mississippi'},
			{'label': 'Missouri','value': 'Missouri'},
			{'label': 'Montana','value': 'Montana'},
			{'label': 'Nebraska','value': 'Nebraska'},
			{'label': 'Nevada','value': 'Nevada'},
			{'label': 'New Hampshire','value': 'New Hampshire'},
			{'label': 'New Jersey','value': 'New Jersey'},
			{'label': 'New Mexico','value': 'New Mexico'},
			{'label': 'New York','value': 'New York'},
			{'label': 'North Carolina','value': 'North Carolina'},
			{'label': 'North Dakota','value': 'North Dakota'},
			{'label': 'Northern Mariana Islands','value': 'Northern Mariana Islands'},
			{'label': 'Ohio','value': 'Ohio'},
			{'label': 'Oklahoma','value': 'Oklahoma'},
			{'label': 'Oregon','value': 'Oregon'},
			{'label': 'Pennsylvania','value': 'Pennsylvania'},
			{'label': 'Puerto Rico','value': 'Puerto Rico'},
			{'label': 'Rhode Island','value': 'Rhode Island'},
			{'label': 'South Carolina','value': 'South Carolina'},
			{'label': 'South Dakota','value': 'South Dakota'},
			{'label': 'Tennessee','value': 'Tennessee'},
			{'label': 'Texas','value': 'Texas'},
			{'label': 'Utah','value': 'Utah'},
			{'label': 'Vermont','value': 'Vermont'},
			{'label': 'Virginia','value': 'Virginia'},
			{'label': 'Virgin Islands','value': 'Virgin Islands'},
			{'label': 'Washington','value': 'Washington'},
			{'label': 'West Virginia','value': 'West Virginia'},
			{'label': 'Wisconsin','value': 'Wisconsin'},
			{'label': 'Wyoming','value': 'Wyoming'}


        ],
        value=['New York'],
        multi=True
),
    dcc.Graph(
        id='bubble-map',
        figure=fig_4
    ),
    html.Label('No mask use by county'),
    dcc.Graph(
        id='mask-use-map',
        figure=fig_2
    ),
    dcc.Graph(
        id='state-cases-bar-graph',
        figure=fig
    ),
    html.Label('Cases V. Deaths'),
    dcc.Graph(
        id='scatterplot',
        figure=fig_3
    ),
    dcc.Graph(
        id='cases-ra',
        figure=fig_5
    ),
    dcc.Graph(
        id='deaths-ra',
        figure=fig_6
    )


])
