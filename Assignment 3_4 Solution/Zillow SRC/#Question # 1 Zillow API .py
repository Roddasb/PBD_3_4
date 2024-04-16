#Question # 1 Zillow API 

import requests
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define function to fetch data from the API
def fetch_data():
    # Define API endpoint, query parameters, and headers
    url = "https://zillow56.p.rapidapi.com/search"
    querystring = {"location": "houston, tx"}
    headers = {
        "X-RapidAPI-Key": "c0c4d833cbmsh57a7250bbb26501p1efb53jsn3afe52d85d8d",
        "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
    }
    # Fetch data from API
    response = requests.get(url, headers=headers, params=querystring)
    # Convert response to JSON format
    return response.json()

# Define function to parse JSON data and return DataFrame
def parse_data(json_data):
    # Normalize JSON data into a DataFrame
    df = pd.json_normalize(json_data['results'])
    return df

# Fetch data from the API
json_data = fetch_data()

# Parse JSON data and create DataFrame
df = parse_data(json_data)

# Define app layout
app.layout = html.Div([
    # Bar chart for distribution of property types
    html.Div([
        dcc.Graph(id='property-type-distribution'),
    ]),
    # Scatter plot for bedrooms vs price
    html.Div([
        dcc.Graph(id='bedrooms-vs-price-scatter'),
    ]),
])

# Define callback to update bar chart for property type distribution
@app.callback(
    Output('property-type-distribution', 'figure'),
    Input('property-type-distribution', 'value')
)
def update_bar_chart(value):
    # Calculate count of each property type
    property_type_counts = df['homeType'].value_counts()

    # Create bar chart
    fig = go.Figure(go.Bar(
        x=property_type_counts.index,
        y=property_type_counts.values,
        marker_color='lightsalmon'
    ))
    fig.update_layout(
        title='Distribution of Property Types',
        xaxis=dict(title='Property Type'),
        yaxis=dict(title='Count'),
        hovermode='x',
    )

    return fig

# Define callback to update scatter plot for bedrooms vs price
@app.callback(
    Output('bedrooms-vs-price-scatter', 'figure'),
    Input('bedrooms-vs-price-scatter', 'value')
)
def update_scatter_plot(value):
    # Create scatter plot for bedrooms vs price
    fig = go.Figure(go.Scatter(
        x=df['bedrooms'],
        y=df['price'],
        mode='markers',
        marker=dict(color='lightskyblue')
    ))
    fig.update_layout(
        title='Bedrooms vs. Price',
        xaxis=dict(title='Number of Bedrooms'),
        yaxis=dict(title='Price ($)'),
        hovermode='closest',
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
