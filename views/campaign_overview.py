import sd_material_ui as sdmui
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Ol import Ol
import dash_bootstrap_components as dbc

from app import app


###############################################################################
# LANDING PAGE LAYOUT
###############################################################################
layout = dbc.Container([

    html.H1('Campaign Optimisation Problem Framing & Overview'),
    html.Hr(),
    html.Br(),

    dbc.Card([
        html.Img(src=app.get_asset_url('Campaign Optimisation - Slide 1.png'), className='center', style={'width': '80%'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Img(src=app.get_asset_url('Campaign Optimisation - Slide 2.png'), className='center', style={'width': '80%'}),
    ], body=True)

], className="mt-4")






