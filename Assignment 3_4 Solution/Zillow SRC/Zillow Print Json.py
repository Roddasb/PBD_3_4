import requests
import dash
from dash import dcc, html
import json

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
    json_data = response.json()
    return json_data, response

# Fetch data from the API
json_data, response = fetch_data()

# Define app layout
app.layout = html.Div([
    # Text area to display the response status code
    html.Div(f"Response Status Code: {response.status_code}"),
    # Text area to display the JSON data
    html.Div(json.dumps(json_data, indent=4)),
])

if __name__ == "__main__":
    app.run_server(debug=True)
