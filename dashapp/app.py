#from data import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

from death_case_graph import fig_0

app.layout = fig_0

#callbacks
df = pd.read_csv('/Users/chris.christie92/Fauci2.0s/Fauci2.0-COVID-19-Dashboard/Fauci2.0-COVID-19-Dashboard/data/us-states.csv')

@app.callback(
    Output('state-cases-bar-graph', 'figure'),
    [Input('dropdown-1', 'value')])
def update_figure(selected_states):
	#print((selected_states))
	new_df = pd.DataFrame()
	for state in selected_states:
		to_append = pd.DataFrame(df[df.state == state])
		new_df = new_df.append(to_append)

	fig = go.Figure()
	fig.add_trace(go.Bar(x=new_df['state'],
                y=new_df['cases'],
                name='Cases by State',
                marker_color='rgb(55, 83, 109)'
                ))
	fig.add_trace(go.Bar(x=new_df['state'],
                y=new_df['deaths'],
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


	#fig = px.bar(new_df, x="state", y="cases", color="state")
	fig.update_layout(transition_duration=500)
	return fig



if __name__ == '__main__':
    app.run_server(debug=True)