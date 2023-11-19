from dash.dependencies import Input, Output
from app import app
from ml import calculate_income, calculate_income_his


@app.callback(
    Output(component_id='dropdown_output', component_property='children'),
    [Input(component_id='dropdown_input', component_property='value')]
)
def update_output(value):
    if not value:
        return "No variables selected."
    else:
        return f"You have selected: {', '.join(value)}"


@app.callback(
    Output(component_id='output', component_property='children'),
    Input(component_id='input_year', component_property='value'),
)
def ml(year):
    return calculate_income(year)


@app.callback(
    Output(component_id='output_his', component_property='children'),
    Input(component_id='input_year', component_property='value'),
)
def ml_his(year):
    return calculate_income_his(year)
