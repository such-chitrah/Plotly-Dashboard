import dash
import dash_bootstrap_components as dbc

# set up app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],)
app.config.suppress_callback_exceptions = True

# name for local test and deployment
app_name = "http://127.0.0.1:8080"
# app_name = "https://stats507-g3.uk.r.appspot.com"

first_color = "#f2eecb"
second_color = "white"
div_style = {
    'backgroundColor': second_color,
    'padding': '20px',
    'borderRadius': '10px',
    'boxShadow': '2px 2px 8px rgba(0, 0, 0, 0.3)'
}
