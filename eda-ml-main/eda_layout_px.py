import data
import plotly.express as px
from dash import html
from dash import dcc
import numpy as np

# separated layouts
income_layout = "todo"
age_layout = "todo"
education_layout = "todo"
politics_layout = "todo"
vehicle_gas_layout = "todo"
home_layout = "todo"
economy_layout = "todo"

# stocks
stocks = data.stocks
# have stock vs income
do_invest = stocks.copy()
do_invest["INCOME"] = do_invest["INCOME"].astype("float64")
do_invest_fig = px.histogram(do_invest.sort_values('INCOME'), x="INCOME", color="INVEST", histfunc='avg', nbins=50, opacity=0.8, color_discrete_sequence=px.colors.qualitative.G10,
                             category_orders={'STL5': ['5', '1']}, labels={'INVEST': 'Have stocks'}, title='Having Stocks vs. Income')
do_invest_fig.update_layout(
    xaxis_title='income',
    yaxis_title='count',
    font=dict(size=12),
    bargap=0.05,
    bargroupgap=0.1
)
do_invest_fig.update_traces(name="Yes", selector={"legendgroup": "1"})
do_invest_fig.update_traces(name="No", selector={"legendgroup": "5"})

# stock percentile vs income
# invest_quintiles = stocks.copy()
# invest_quintiles["INCOME"] = invest_quintiles["INCOME"].astype("float64")
# invest_quintiles_fig = px.histogram(invest_quintiles.sort_values('INCOME'), x='INCOME', color='STL5', nbins=50, opacity=0.8, color_discrete_sequence=px.colors.qualitative.G10,
# category_orders = {'STL5': ['5', '4', '3', '2', '1']}, labels = {'STL5': 'Stock Percentiles (Quintiles)'}, title = 'Stock Percentiles vs. Income')

# invest_quintiles_fig.update_layout(
# xaxis_title='income',
# yaxis_title='count',
# font=dict(size=12),
# bargap=0.05,
# bargroupgap=0.1
# )

# invest_quintiles_fig.update_traces(
# name="Bottom 20%", selector={"legendgroup": "1"})
# invest_quintiles_fig.update_traces(
# name="21-40%", selector={"legendgroup": "2"})
# invest_quintiles_fig.update_traces(
#     name="41-60%", selector={"legendgroup": "3"})
# invest_quintiles_fig.update_traces(
# name="61-80%", selector={"legendgroup": "4"})
# invest_quintiles_fig.update_traces(
# name="Top 20%", selector={"legendgroup": "5"})

# investment vs income
invest = stocks.copy()
invest["INCOME"] = invest["INCOME"].astype("float64")
invest["INCOME"] = invest["INCOME"].astype("float64")
invest["INVAMT"] = invest["INVAMT"].astype("float64")
invest["INVEST_INCOME_RATIO"] = invest["INVAMT"]/invest["INCOME"]
invest_fig = px.histogram(invest.sort_values('INCOME'), x="INCOME", y="INVAMT", histfunc='avg', nbins=50,
                          opacity=0.8, color_discrete_sequence=['#008080'], title='Investment in Stock Markets vs. Income')
invest_fig.update_layout(
    xaxis_title='income',
    yaxis_title='investment in stock markets',
    font=dict(size=12),
    bargap=0.05,
    bargroupgap=0.1
)

# confidenc in stock markets vs income
pstk = stocks.copy()
pstk.loc[(pstk["PSTK"] == '999.0'), "PSTK"] = np.nan
pstk.loc[(pstk["PSTK"] == '998.0'), "PSTK"] = np.nan
pstk = pstk[pstk["PSTK"].notna()]
pstk["INCOME"] = pstk["INCOME"].astype("float64")
pstk["PSTK"] = pstk["PSTK"].astype("float64")

pstk_fig = px.histogram(pstk, x="INCOME", y="PSTK", histfunc='avg', nbins=50, opacity=0.8,
                        color_discrete_sequence=['#008080'], title='Confidence in Stock Markets vs. Income')
pstk_fig.update_layout(
    xaxis_title='income',
    yaxis_title='percent chance of invest increase in 1 year',
    font=dict(size=12),
    bargap=0.05,
    bargroupgap=0.1
)

stocks_layout = html.Div([
    dcc.Graph(
        id='do_income_fig',
        figure=do_invest_fig
    ),
    dcc.Graph(
        id='invest_fig',
        figure=invest_fig
    ),
    dcc.Graph(
        id='pstk_fig',
        figure=pstk_fig
    ),
])

# layout summary
eda_layout_px = html.Div([income_layout, age_layout, education_layout,
                         stocks_layout, politics_layout, vehicle_gas_layout, economy_layout])
