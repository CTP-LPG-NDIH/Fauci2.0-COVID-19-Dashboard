import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# App Layout

#import graph figures here
from death_case_graph import fig, fig_7, fig_8, fig_9, fig_10
from mask_usage import fig_2
from scatter import fig_3
from scatter_geo import fig_4
from rolling_avg import fig_5,fig_6
from airport_map import fig_11


cards_1 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Intl. Airports Volume in the U.S", className="card-title"),
                    html.P(
                        "Volume of International Airports may play "
                        "a key role in the case growth of certain states.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="success", className="mt-auto"
                    ),
					dcc.Graph(figure=fig_11)
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Cumulative Death Counts in the United States", className="card-title"),
                    html.P(
                        "The total number of cases in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="warning", className="mt-auto"
                    ),
					dcc.Graph(figure=fig_6)
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Cumulative Case Counts in the United States", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(

                    #    "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(figure=fig_5)
                ]
            )
        ),
    ]
)

cards_2 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Death Increases Counts in the United States", className="card-title"),
                    html.P(
                        "The total number of death increases in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(id='death-increases', figure=fig_10)
                ]
            )
        ),
    ]
)

cards_3 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("No. of People Hospitalized in the U.S", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(figure=fig_8)
                ]
            )
        ),
		dbc.Card(
            dbc.CardBody(
                [
                    html.H5("No. of People Currently Hospitalized", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(figure=fig_9)
                ]
            )
        ),
    ]
)

cards_4 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("No. of People Hospitalized in the U.S", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(id= 'state-cases-bar-graph', figure=fig)
                ]
            )
        ),
		dbc.Card(
            dbc.CardBody(
                [
                    html.H5("No. of People Currently Hospitalized", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(id='mask-use-map', figure=fig_2)
                ]
            )
        ),
    ]
)

cards_5 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("No. of People Hospitalized in the U.S", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(id='scatterplot', figure=fig_3)
                ]
            )
        ),
		dbc.Card(
            dbc.CardBody(
                [
                    html.H5("No. of People Currently Hospitalized", className="card-title"),
                    html.P(
                        "The total number of deaths in the United States over time.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Click here", color="danger", className="mt-auto"
                    ),
					dcc.Graph(id='bubble-map', figure=fig_4)
                ]
            )
        ),
    ]
)




navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home Page", href="#")),
        dbc.DropdownMenu(
			children=[
				dbc.DropdownMenuItem("More", header=True),
				dbc.DropdownMenuItem("Page 2", href="#"),
				dbc.DropdownMenuItem("Page 3", href="#"),
			],
            nav=True,
            in_navbar=True,
            label="More Pages",
        ),
    ],
    brand="COVID-19 Dash-Board",
    brand_href="#",
    color="primary",
    dark=True,
)



fig_0 = html.Div(children=[
	navbar,
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
        value=['New York','Florida','Texas','California','Illinois'],
        multi=True
),

    dbc.Row([dbc.Col(cards_4)]),
    dbc.Row([dbc.Col(cards_5)]),
	dbc.Row([dbc.Col(cards_1)]),
	dbc.Row([dbc.Col(cards_2)]),
	dbc.Row([dbc.Col(cards_3)]),

])
