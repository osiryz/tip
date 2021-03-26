import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Month": ["201801", "201802", "201803", "201801", "201802", "201803", "201801", "201802", "201803", "201801", "201802", "201803"],
    "Incidences": [300, 287, 292, 7706, 6486, 6630, 2382, 2344, 2353, 13, 18, 9],
    "Priority": ["Alta", "Alta", "Alta", "Baja", "Baja", "Baja", "Media", "Media", "Media", "Crit", "Crit", "Crit"]
})

def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")

    

    dash_app.layout = html.Div(children=[
        html.H1(children='Hello MCSBT'),

        html.Div(children='''
            Term Integration Platform - Iberia.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=px.bar(df, x="Month", y="Incidences", color="Priority", barmode="group")
        )
    ])
    return dash_app