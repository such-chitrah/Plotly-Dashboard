from dash import html
from dash import dcc


# separated layout
income_layout = html.Div([
    html.H2("Predict the average income according to..."),
    html.Div([
        "Enter the year for prediction: ",
        dcc.Input(id='input_year', value='2020', type='text',
                  style={"margin-left": "10px"}),
    ]),
    html.Br(),
    html.Div(["The predicted average income is:   ", html.Div(
        id='output', style={"margin-left": "10px"})], style={"display": "inline-flex"}),
    html.Br(),
    html.Br(),
    html.Div(["The exact value is:   ", html.Div(
        id='output_his', style={"margin-left": "10px"})], style={"display": "inline-flex"}),
])

dropdown_layout = html.Div([
    dcc.Markdown(
        "Select the considered varibles that are used for prediciton:"),
    dcc.Dropdown(
        options=[
            {"label": "income", "value": "income"},
            {"label": "education", "value": "education"},
            {"label": "stocks", "value": "stocks"},
        ],
        value=["income", "education"],
        multi=True,
        id='dropdown_input',
    ),
    html.Div(id='dropdown_output')
])


# layout for the prediciton page
prediction_layout = html.Div([income_layout, html.Br(), dropdown_layout])
