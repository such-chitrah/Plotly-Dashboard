import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app, app_name
import callbacks
from navbar import Navbar
from eda_layout_px import eda_layout_px
from eda_layout_plt import eda_layout_plt
from models_layout import models_layout
from prediction_layout import prediction_layout

server = app.server
# layout, navbar, header, content, and container
nav = Navbar()
header = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H2(
                    children="Social Associations with Income: A Pre-Pandemic Analysis"),
            ]
        )
    ),
    className="banner",
)
content = html.Div([dcc.Location(id="url"), html.Div(id="page-content")])
container = dbc.Container([header, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname in [app_name, app_name + "/", "/"]:
        return html.Div(
            [
                dcc.Markdown(
                    """
            ### some info
            todo
        """
                )
            ],
            className="home",
        )
    elif pathname.endswith("/eda"):
        return eda_layout_px, eda_layout_plt
    elif pathname.endswith("/models"):
        return models_layout
    elif pathname.endswith("/prediction"):
        return prediction_layout
    else:
        return "ERROR 404: Page not found!"


def index():
    layout = html.Div([nav, container])
    return layout


app.layout = index()


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
