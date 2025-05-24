html.Himport dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={
            'textAlign': 'center',
            'color': '#503D36',
            'font-size': '24px'
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True) 
    