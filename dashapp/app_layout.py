import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# App Layout

#import graph figures here
from death_case_graph import fig, fig_7, fig_8, fig_9, fig_10
from mask_usage import fig_2
from scatter import fig_3
from scatter_geo import fig_4
from rolling_avg import fig_5,fig_6
from airport_map import fig_11


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
    html.Label('Mask use by county'),
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
	html.Label('Cumulative Case Counts in the U.S'),
	dcc.Graph(
        id='cases-ra',
        figure=fig_5
    ),
	html.Label('Cumulative Death Counts in the U.S'),
	dcc.Graph(
        id='deaths-ra',
        figure=fig_6
    ),
	html.Label('State Line Graph of Positive Cases'),
	dcc.Graph(
		id='state-positives',
		figure=fig_7
	),
	html.Label('No. of People Hospitalized'),
	dcc.Graph(
		id='hospitalized',
		figure=fig_8
	),
	html.Label('No. of People Hospitalized Currently'),
	dcc.Graph(
		id='hospitalized-currently',
		figure=fig_9
	),
	html.Label('State Death Increases'),
	dcc.Graph(
		id='death-increases',
		figure=fig_10
	),
	dcc.Graph(
		id='airport-map',
		figure=fig_11
	),



])