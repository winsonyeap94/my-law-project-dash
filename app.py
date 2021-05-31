# Dash app initialization
import dash
import dash_bootstrap_components as dbc
# User management initialization
import os

from conf.config import config


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
server = app.server
app.config.suppress_callback_exceptions = True


