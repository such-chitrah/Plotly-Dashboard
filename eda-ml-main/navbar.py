import dash_bootstrap_components as dbc
from app import app_name, first_color


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(
                "EDA", href=f"{app_name}/eda", style={'font-size': '20px'})),
            dbc.NavItem(dbc.NavLink(
                "Models", href=f"{app_name}/models", style={'font-size': '20px'})),
            dbc.NavItem(dbc.NavLink(
                "Prediction", href=f"{app_name}/prediction", style={'font-size': '20px'})),
        ],
        brand="HOME",
        brand_href=f"{app_name}",
        sticky="top",
        color=first_color,
        dark=False,
    )
    return navbar
