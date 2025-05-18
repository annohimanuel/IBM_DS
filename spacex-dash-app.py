from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Read the SpaceX data into a DataFrame
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Get min and max payloads
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Initialize the Dash app
app = Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),

    # Dropdown for Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'}
        ] + [{'label': site, 'value': site} for site in spacex_df["Launch Site"].unique()],
        value='ALL',
        placeholder='Select a Launch Site',
        searchable=True
    ),
    html.Br(),

    # Pie chart for launch outcomes
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # Payload range slider
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        value=[min_payload, max_payload],
        marks={i: f'{i} Kg' for i in range(0, 10001, 1000)}
    ),

    # Scatter plot
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# Callback to update the pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Count total successes per launch site
        fig_data = spacex_df[spacex_df['class'] == 1]['Launch Site'].value_counts().reset_index()
        fig_data.columns = ['Launch Site', 'Success Count']
        fig = px.pie(fig_data, names='Launch Site', values='Success Count',
                     title='Total Successful Launches by Site')
    else:
        # Show Success vs Failure for the selected site
        site_data = spacex_df[spacex_df['Launch Site'] == selected_site]
        outcome_counts = site_data['class'].value_counts().reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        outcome_counts['Outcome'] = outcome_counts['Outcome'].replace({1: 'Success', 0: 'Failure'})
        fig = px.pie(outcome_counts, names='Outcome', values='Count',
                     title=f'Success vs Failure for {selected_site}')
    return fig

# Callback to update the scatter plot
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [
        Input('site-dropdown', 'value'),
        Input('payload-slider', 'value')
    ]
)
def update_scatter_chart(selected_site, selected_payload):
    low, high = selected_payload
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) &
                             (spacex_df['Payload Mass (kg)'] <= high)]

    if selected_site == 'ALL':
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Correlation between Payload and Success for All Sites'
        )
    else:
        site_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(
            site_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Correlation between Payload and Success for {selected_site}'
        )

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8060)

